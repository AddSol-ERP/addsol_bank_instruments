# Copyright (c) 2024, AddSol and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt


class LCAmendment(Document):
	def validate(self):
		self.fetch_lc_details()
		self.calculate_amount_change()
		self.set_amendment_number()
	
	def fetch_lc_details(self):
		"""Fetch details from the original LC"""
		if self.letter_of_credit:
			lc = frappe.get_doc("Letter of Credit", self.letter_of_credit)
			
			# Set previous values
			self.previous_lc_amount = lc.lc_amount
			self.previous_expiry_date = lc.expiry_date
			self.previous_shipment_date = lc.latest_shipment_date
	
	def calculate_amount_change(self):
		"""Calculate the amount change"""
		if self.new_lc_amount and self.previous_lc_amount:
			self.amount_change = flt(self.new_lc_amount) - flt(self.previous_lc_amount)
	
	def set_amendment_number(self):
		"""Auto-set amendment number"""
		if not self.amendment_number and self.letter_of_credit:
			# Count existing amendments
			count = frappe.db.count(
				"LC Amendment",
				filters={
					"letter_of_credit": self.letter_of_credit,
					"docstatus": ["!=", 2]
				}
			)
			self.amendment_number = count + 1
	
	def on_submit(self):
		"""Update the LC with amended values"""
		if self.letter_of_credit:
			lc = frappe.get_doc("Letter of Credit", self.letter_of_credit)
			
			# Update LC values
			if self.new_lc_amount:
				lc.lc_amount = self.new_lc_amount
			
			if self.new_expiry_date:
				lc.expiry_date = self.new_expiry_date
			
			if self.new_shipment_date:
				lc.latest_shipment_date = self.new_shipment_date
			
			# Update status
			lc.status = "Amended"
			
			# Save without validating to avoid recursion
			lc.flags.ignore_validate = True
			lc.save()
			
			# Add comment to LC
			lc.add_comment(
				"Info",
				f"LC amended via {self.name}. Amendment Type: {self.amendment_type}"
			)
			
			# Update amendment status
			self.status = "Approved"
			self.save()
	
	def on_cancel(self):
		"""Revert LC to previous values"""
		if self.letter_of_credit:
			lc = frappe.get_doc("Letter of Credit", self.letter_of_credit)
			
			# Revert to previous values
			if self.previous_lc_amount:
				lc.lc_amount = self.previous_lc_amount
			
			if self.previous_expiry_date:
				lc.expiry_date = self.previous_expiry_date
			
			if self.previous_shipment_date:
				lc.latest_shipment_date = self.previous_shipment_date
			
			# Save without validating
			lc.flags.ignore_validate = True
			lc.save()
			
			# Add comment
			lc.add_comment("Info", f"Amendment {self.name} cancelled and reverted")
			
			# Update status
			self.status = "Cancelled"
			self.save()