# Copyright (c) 2024, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, today, add_days
from frappe import _


class LetterofCredit(Document):
	def validate(self):
		self.validate_dates()
		self.validate_parties()
		self.calculate_balance_amount()
		self.update_status()
		self.set_expiry_within_30_days()
		# Validate Naming Series
		if self.transaction_type == "Import":
			self.naming_series = "LC-IMP-.YYYY.-"
		elif self.transaction_type == "Export":
			self.naming_series = "LC-EXP-.YYYY.-"
	
	def validate_dates(self):
		"""Validate LC dates"""
		if self.expiry_date and self.lc_date:
			if getdate(self.expiry_date) < getdate(self.lc_date):
				frappe.throw("Expiry Date cannot be before LC Opening Date")
		
		if self.latest_shipment_date and self.lc_date:
			if getdate(self.latest_shipment_date) < getdate(self.lc_date):
				frappe.throw("Latest Shipment Date cannot be before LC Opening Date")
		
		if self.latest_shipment_date and self.expiry_date:
			if getdate(self.latest_shipment_date) > getdate(self.expiry_date):
				frappe.throw("Latest Shipment Date cannot be after Expiry Date")
	
	def validate_parties(self):
		"""Validate applicant and beneficiary"""
		if self.transaction_type == "Import":
			if self.applicant_type != "Company":
				frappe.throw("For Import LC, Applicant Type must be Company")
			if self.beneficiary_type != "Supplier":
				frappe.throw("For Import LC, Beneficiary Type must be Supplier")
		elif self.transaction_type == "Export":
			if self.applicant_type != "Customer":
				frappe.throw("For Export LC, Applicant Type must be Customer")
			if self.beneficiary_type != "Company":
				frappe.throw("For Export LC, Beneficiary Type must be Company")
	
	def calculate_balance_amount(self):
		"""Calculate balance amount from LC amount and utilized amount"""
		self.utilized_amount = flt(self.utilized_amount)
		self.lc_amount = flt(self.lc_amount)
		
		# Calculate utilized amount from shipments
		total_shipped = 0
		if self.shipments:
			for shipment in self.shipments:
				total_shipped += flt(shipment.shipped_value)
		
		self.utilized_amount = total_shipped
		
		# Calculate tolerance
		tolerance_amount = flt(self.lc_amount) * flt(self.tolerance_percentage) / 100
		max_lc_amount = flt(self.lc_amount) + tolerance_amount
		
		# Calculate balance
		self.balance_amount = max_lc_amount - flt(self.utilized_amount)
		
		# Validate utilized amount doesn't exceed LC amount + tolerance
		if self.utilized_amount > max_lc_amount:
			frappe.throw(
				f"Utilized Amount ({self.utilized_amount}) cannot exceed LC Amount + Tolerance ({max_lc_amount})"
			)
	
	def update_status(self):
		"""Auto-update status based on conditions"""
		if self.docstatus == 0:  # Draft
			return
		
		# Check if expired
		if self.expiry_date and getdate(self.expiry_date) < getdate():
			if self.status not in ["Settled", "Cancelled"]:
				self.status = "Expired"
			return
		
		# Check if all documents are accepted
		all_accepted = True
		if self.documents:
			for doc in self.documents:
				if doc.submission_status != "Accepted":
					all_accepted = False
					break
		
		# Update status based on shipments and documents
		if self.shipments and len(self.shipments) > 0:
			if all_accepted and self.status == "Documents Submitted":
				self.status = "Documents Accepted"
		
		# Check if fully utilized
		if flt(self.balance_amount) <= 0:
			if self.status == "Documents Accepted":
				self.status = "Settled"
	
	def set_expiry_within_30_days(self):
		"""Set expiry within 30 days"""
		if self.expiry_date:
			self.expiry_within_30_days = (
				self.expiry_date >= today()
				and self.expiry_date <= add_days(today(), 30)
			)
		else:
			self.expiry_within_30_days = 0

	def on_submit(self):
		"""On submit, set status to Opened and send notification"""
		if self.status == "Draft":
			self.status = "Opened"
			self.save()
		self.send_notification()
	
	def on_cancel(self):
		"""On cancel, set status and send notification"""
		self.status = "Cancelled"
		self.save()
		self.send_cancellation_notification()
	
	def send_notification(self):
		"""Send notification on submission"""
		recipients = self.get_notification_recipients()
		
		if recipients:
			subject = _("LC {0} - {1} has been opened").format(
				self.lc_number, self.transaction_type
			)
			
			message = frappe.render_template(
				"addsol_bank_instruments/templates/emails/lc_notification.html",
				{"doc": self}
			)
			
			frappe.sendmail(
				recipients=recipients,
				subject=subject,
				message=message,
				reference_doctype=self.doctype,
				reference_name=self.name
			)
	
	def send_cancellation_notification(self):
		"""Send notification on cancellation"""
		recipients = self.get_notification_recipients()
		
		if recipients:
			subject = _("LC {0} - {1} has been cancelled").format(
				self.lc_number, self.transaction_type
			)
			
			message = _("Letter of Credit {0} has been cancelled by {1}").format(
				self.lc_number, frappe.session.user
			)
			
			frappe.sendmail(
				recipients=recipients,
				subject=subject,
				message=message,
				reference_doctype=self.doctype,
				reference_name=self.name
			)
	
	def get_notification_recipients(self):
		"""Get list of users to notify"""
		recipients = []
		
		# Get all users with Accounts Manager role
		accounts_managers = frappe.get_all(
			"Has Role",
			filters={"role": "Accounts Manager", "parenttype": "User"},
			fields=["parent"]
		)
		
		for manager in accounts_managers:
			user_email = frappe.db.get_value("User", manager.parent, "email")
			if user_email:
				recipients.append(user_email)
		
		return list(set(recipients))  # Remove duplicates


# Scheduled notification functions
def send_lc_expiry_notifications():
    """
    Daily scheduled job to send LC expiry notifications
    Call this from Hooks: Scheduler Events
    """
    try:
        # Get LCs expiring in 30, 15, 7, 3, 1 days
        notification_days = [30, 15, 7, 3, 1]
        
        for days in notification_days:
            target_date = add_days(today(), days)
            
            # Optimized query - filter by date directly in database
            lcs = frappe.get_all(
                "Letter of Credit",
                filters=[
                    ["docstatus", "=", 1],
                    ["status", "in", ["Opened", "Amended", "Documents Submitted", "Documents Accepted", "Payment Made"]],
                    ["expiry_date", "=", target_date]
                ],
                fields=["name", "lc_number", "expiry_date", "transaction_type", "lc_type", "beneficiary_name", "lc_amount", "currency"]
            )
            
            for lc in lcs:
                try:
                    send_lc_expiry_alert(lc.name, days)
                except Exception as e:
                    frappe.log_error(f"Failed to send expiry alert for LC {lc.name}: {str(e)}", "LC Notification Error")
                    
    except Exception as e:
        frappe.log_error(f"Error in send_lc_expiry_notifications: {str(e)}", "LC Notification System Error")


def send_lc_expiry_alert(lc_name, days_remaining):
    """Send expiry alert email for LC"""
    try:
        doc = frappe.get_doc("Letter of Credit", lc_name)
        recipients = doc.get_notification_recipients()
        
        if recipients:
            subject = _("🚨 LC {0} expiring in {1} days").format(
                doc.lc_number, days_remaining
            )
            
            message = frappe.render_template(
                "addsol_bank_instruments/templates/emails/lc_expiry_alert.html",
                {"doc": doc, "days_remaining": days_remaining}
            )
            
            frappe.sendmail(
                recipients=recipients,
                subject=subject,
                message=message,
                reference_doctype=doc.doctype,
                reference_name=doc.name
            )
            
            # Log successful notification
            frappe.logger().info(f"Expiry alert sent for LC {doc.lc_number} ({days_remaining} days remaining)")
            
    except Exception as e:
        frappe.log_error(f"Failed to send expiry alert for LC {lc_name}: {str(e)}", "LC Expiry Alert Error")
        raise