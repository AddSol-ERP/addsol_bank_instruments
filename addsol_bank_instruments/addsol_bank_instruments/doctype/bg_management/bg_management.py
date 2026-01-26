# Copyright (c) 2025, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import (
    getdate, 
    today, 
    date_diff, 
    add_days, 
    flt,
    nowdate,
    get_datetime
)
from datetime import datetime, timedelta


class BGManagement(Document):
    def validate(self):
        self.set_default_company()
        self.validate_dates()
        self.validate_sales_purchase_order()
        self.calculate_days_to_expiry()
        self.calculate_available_amount()
        self.calculate_charges()
        self.update_status()
        self.validate_utilized_amount()
    
    def validate_sales_purchase_order(self):
        """Validate that Sales Order and Purchase Order cannot both have values"""
        if self.sales_order and self.purchase_order:
            frappe.throw(_("Both Sales Order and Purchase Order cannot be specified simultaneously. Please specify only one."))
    
    def set_default_company(self):
        """Set default company if not specified"""
        if not self.applicant:
            default_company = frappe.defaults.get_user_default('Company')
            if default_company:
                self.applicant = default_company
        
    def before_submit(self):
        if not self.fd_number:
            frappe.throw(_("FD Number is mandatory before submission"))
        if not self.bg_document:
            frappe.throw(_("Please attach BG Document before submission"))
            
    def on_submit(self):
        self.create_journal_entry_for_fd()
        self.send_notification()
        
    def on_cancel(self):
        self.status = "Cancelled"
        self.send_cancellation_notification()
    
    def validate_dates(self):
        """Validate all date fields"""
        if getdate(self.expiry_date) <= getdate(self.issue_date):
            frappe.throw(_("Expiry Date must be after Issue Date"))
            
        if self.fd_maturity_date and getdate(self.fd_maturity_date) < getdate(self.expiry_date):
            frappe.throw(_("FD Maturity Date should be on or after BG Expiry Date"))
            
        if self.is_extended and self.extension_expiry_date:
            if getdate(self.extension_expiry_date) <= getdate(self.expiry_date):
                frappe.throw(_("Extension Expiry Date must be after Original Expiry Date"))
    
    def calculate_days_to_expiry(self):
        """Calculate days remaining to expiry"""
        effective_expiry = self.extension_expiry_date if self.is_extended else self.expiry_date
        if effective_expiry:
            self.days_to_expiry = date_diff(effective_expiry, today())
    
    def calculate_available_amount(self):
        """Calculate available amount"""
        self.available_amount = flt(self.maturity_amount) - flt(self.utilized_amount)
        
    def calculate_charges(self):
        """Calculate commission and total charges"""
        if self.commission_rate and self.fd_amount:
            self.commission_amount = flt(self.fd_amount) * flt(self.commission_rate) / 100
        else:
            self.commission_amount = 0
            
        self.total_charges = flt(self.commission_amount) + flt(self.processing_charges)
    
    def update_status(self):
        """Auto-update status based on dates and conditions"""
        if self.docstatus == 2:  # Cancelled
            self.status = "Cancelled"
            return
            
        if self.claim_date:
            self.status = "Claimed"
            return
            
        effective_expiry = self.extension_expiry_date if self.is_extended else self.expiry_date
        
        if effective_expiry:
            if getdate(effective_expiry) < getdate(today()):
                self.status = "Expired"
            elif self.is_extended:
                self.status = "Extended"
            elif flt(self.available_amount) <= 0:
                self.status = "Closed"
            else:
                self.status = "Active"
    
    def validate_utilized_amount(self):
        """Validate that utilized amount doesn't exceed maturity amount"""
        if flt(self.utilized_amount) > flt(self.maturity_amount):
            frappe.throw(_("Utilized Amount cannot exceed Maturity Amount"))
    
    def create_journal_entry_for_fd(self):
        """Create Journal Entry for FD blocking (optional automation)"""
        # This is a placeholder - implement based on your accounting setup
        pass
    
    def send_notification(self):
        """Send notification on submission"""
        recipients = self.get_notification_recipients()
        
        if recipients:
            subject = _("BG Management {0} - {1} has been submitted").format(
                self.bg_number, self.bg_type
            )
            
            message = frappe.render_template(
                "addsol_bank_instruments/templates/emails/bg_management_notification.html",
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
            subject = _("BG Management {0} - {1} has been cancelled").format(
                self.bg_number, self.bg_type
            )
            
            message = _("BG Management {0} has been cancelled by {1}").format(
                self.bg_number, frappe.session.user
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


@frappe.whitelist()
def extend_bg_management(bg_management_name, new_expiry_date, extension_charges=0, remarks=None):
    """
    Extend a BG Management record
    """
    doc = frappe.get_doc("BG Management", bg_management_name)
    
    if doc.docstatus != 1:
        frappe.throw(_("Only submitted BG Management records can be extended"))
    
    # Get current expiry date
    current_expiry = doc.extension_expiry_date if doc.is_extended else doc.expiry_date
    
    # Validate new expiry date
    if getdate(new_expiry_date) <= getdate(current_expiry):
        frappe.throw(_("New Expiry Date must be after current expiry date"))
    
    # Calculate extension days
    extension_days = date_diff(new_expiry_date, current_expiry)
    
    # Calculate extension number
    extension_number = len(doc.extension_history) + 1
    
    # Add to extension history
    doc.append("extension_history", {
        "extension_number": extension_number,
        "previous_expiry_date": current_expiry,
        "new_expiry_date": new_expiry_date,
        "extension_days": extension_days,
        "extension_date": today(),
        "extension_charges": extension_charges,
        "approved_by": frappe.session.user,
        "remarks": remarks
    })
    
    # Update main fields
    doc.is_extended = 1
    doc.extension_expiry_date = new_expiry_date
    doc.status = "Extended"
    
    # Save changes
    doc.save(ignore_permissions=True)
    
    frappe.msgprint(_("BG Management extended successfully to {0}").format(new_expiry_date))
    
    return doc.name


@frappe.whitelist()
def mark_as_claimed(bg_management_name, claim_date=None, claim_amount=0):
    """
    Mark BG Management as Claimed
    """
    doc = frappe.get_doc("BG Management", bg_management_name)
    
    if doc.docstatus != 1:
        frappe.throw(_("Only submitted BG Management records can be marked as claimed"))
    
    doc.claim_date = claim_date or today()
    doc.status = "Claimed"
    
    if claim_amount:
        doc.utilized_amount = flt(doc.utilized_amount) + flt(claim_amount)
    
    doc.save(ignore_permissions=True)
    
    frappe.msgprint(_("BG Management marked as claimed"))
    
    return doc.name


@frappe.whitelist()
def close_bg_management(bg_management_name, remarks=None):
    """
    Close a BG Management record
    """
    doc = frappe.get_doc("BG Management", bg_management_name)
    
    if doc.docstatus != 1:
        frappe.throw(_("Only submitted BG Management records can be closed"))
    
    if doc.status == "Claimed":
        frappe.throw(_("Claimed BG Management records cannot be closed. Please cancel instead."))
    
    doc.status = "Closed"
    if remarks:
        doc.internal_notes = (doc.internal_notes or "") + "\n\n" + remarks
    
    doc.save(ignore_permissions=True)
    
    frappe.msgprint(_("BG Management closed successfully"))
    
    return doc.name


def send_expiry_notifications():
    """
    Daily scheduled job to send expiry notifications
    Call this from Hooks: Scheduler Events
    """
    try:
        # Get BGs expiring in 30, 15, 7, 3, 1 days
        notification_days = [30, 15, 7, 3, 1]
        
        for days in notification_days:
            target_date = add_days(today(), days)
            
            # Optimized query - filter by date directly in database
            bgs = frappe.get_all(
                "BG Management",
                filters=[
                    ["docstatus", "=", 1],
                    ["status", "in", ["Active", "Extended"]],
                    ["expiry_date", "=", target_date]
                ],
                fields=["name", "bg_number", "expiry_date", "extension_expiry_date", "is_extended", "bg_type", "beneficiary_name", "fd_amount"]
            )
            
            # Also check extended expiry dates
            extended_bgs = frappe.get_all(
                "BG Management",
                filters=[
                    ["docstatus", "=", 1],
                    ["status", "=", "Extended"],
                    ["extension_expiry_date", "=", target_date]
                ],
                fields=["name", "bg_number", "expiry_date", "extension_expiry_date", "is_extended", "bg_type", "beneficiary_name", "fd_amount"]
            )
            
            # Combine both lists
            all_bgs = bgs + extended_bgs
            
            for bg in all_bgs:
                try:
                    send_expiry_alert(bg.name, days)
                except Exception as e:
                    frappe.log_error(f"Failed to send expiry alert for BG {bg.name}: {str(e)}", "BG Notification Error")
                    
    except Exception as e:
        frappe.log_error(f"Error in send_expiry_notifications: {str(e)}", "BG Notification System Error")


def send_expiry_alert(bg_management_name, days_remaining):
    """Send expiry alert email"""
    try:
        doc = frappe.get_doc("BG Management", bg_management_name)
        recipients = doc.get_notification_recipients()
        
        if recipients:
            subject = _("🚨 BG Management {0} expiring in {1} days").format(
                doc.bg_number, days_remaining
            )
            
            message = frappe.render_template(
                "addsol_bank_instruments/templates/emails/bg_expiry_alert.html",
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
            frappe.logger().info(f"Expiry alert sent for BG {doc.bg_number} ({days_remaining} days remaining)")
            
    except Exception as e:
        frappe.log_error(f"Failed to send expiry alert for BG {bg_management_name}: {str(e)}", "BG Expiry Alert Error")
        raise


def get_permission_query_conditions(user):
    """Permission query conditions for BG Management"""
    if not user:
        user = frappe.session.user
    
    # If user is System Manager, no restrictions
    if "System Manager" in frappe.get_roles(user):
        return None
    
    # If user has Accounts roles, they can see all BG records
    user_roles = frappe.get_roles(user)
    if any(role in ["Accounts Manager", "Accounts User"] for role in user_roles):
        return None
    
    # Otherwise, restrict to documents they created
    return f"`tabBG Management`.owner = '{user}'"


def has_permission(doc, ptype, user):
    """Check if user has permission for BG Management document"""
    if not user:
        user = frappe.session.user
    
    # System Manager has all permissions
    if "System Manager" in frappe.get_roles(user):
        return True
    
    # Accounts roles have all permissions except cancel
    user_roles = frappe.get_roles(user)
    if any(role in ["Accounts Manager", "Accounts User"] for role in user_roles):
        if ptype == "cancel":
            return "Accounts Manager" in user_roles
        return True
    
    # Other users can only view their own documents
    if ptype in ["read", "write"]:
        return doc.owner == user
    
    return False

def validate_bg(doc, method):
    """Hook function for BG Management validation"""
    # Additional validation logic can be added here
    pass

def on_bg_submit(doc, method):
    """Hook function called when BG Management is submitted"""
    frappe.msgprint(_("Bank Guarantee {0} has been submitted successfully").format(doc.bg_number))

def on_bg_cancel(doc, method):
    """Hook function called when BG Management is cancelled"""
    frappe.msgprint(_("Bank Guarantee {0} has been cancelled").format(doc.bg_number))
