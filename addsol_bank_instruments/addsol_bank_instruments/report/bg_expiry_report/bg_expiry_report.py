# Copyright (c) 2026, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, date_diff, today


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart_data(data)
	return columns, data, None, chart


def get_columns():
	return [
		{
			"fieldname": "name",
			"label": _("BG Number"),
			"fieldtype": "Link",
			"options": "BG Management",
			"width": 150
		},
		{
			"fieldname": "bg_type",
			"label": _("BG Type"),
			"fieldtype": "Data",
			"width": 120
		},
		{
			"fieldname": "applicant",
			"label": _("Applicant"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "beneficiary_name",
			"label": _("Beneficiary"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "issue_date",
			"label": _("Issue Date"),
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "expiry_date",
			"label": _("Expiry Date"),
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "days_to_expiry",
			"label": _("Days to Expiry"),
			"fieldtype": "Int",
			"width": 120
		},
		{
			"fieldname": "expiry_status",
			"label": _("Expiry Status"),
			"fieldtype": "Data",
			"width": 120
		},
		{
			"fieldname": "fd_amount",
			"label": _("FD Amount"),
			"fieldtype": "Currency",
			"width": 120
		},
		{
			"fieldname": "maturity_amount",
			"label": _("Maturity Amount"),
			"fieldtype": "Currency",
			"width": 130
		},
		{
			"fieldname": "utilized_amount",
			"label": _("Utilized Amount"),
			"fieldtype": "Currency",
			"width": 130
		},
		{
			"fieldname": "available_amount",
			"label": _("Available Amount"),
			"fieldtype": "Currency",
			"width": 130
		},
		{
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Data",
			"width": 120
		},
		{
			"fieldname": "bank",
			"label": _("Issuing Bank"),
			"fieldtype": "Data",
			"width": 150
		}
	]


def get_data(filters):
	conditions = get_conditions(filters)
	
	data = frappe.db.sql("""
		SELECT
			bg.name,
			bg.bg_type,
			bg.applicant,
			bg.beneficiary_name,
			bg.issue_date,
			bg.expiry_date,
			bg.fd_amount,
			bg.maturity_amount,
			bg.utilized_amount,
			bg.available_amount,
			bg.status,
			bg.bank
		FROM
			`tabBG Management` bg
		WHERE
			bg.docstatus = 1
			AND bg.status NOT IN ('Cancelled', 'Closed')
			{conditions}
		ORDER BY
			bg.expiry_date ASC
	""".format(conditions=conditions), filters, as_dict=1)
	
	# Calculate days to expiry and expiry status
	for row in data:
		# Use effective expiry date (consider extensions)
		effective_expiry = row.expiry_date
		if row.status == 'Extended':
			# Get extension expiry date if extended
			extension_expiry = frappe.db.get_value('BG Management Extension', 
				{'parent': row.name}, ['new_expiry_date'], order_by='creation desc')
			if extension_expiry:
				effective_expiry = extension_expiry[0]
		
		if effective_expiry:
			days = date_diff(effective_expiry, today())
			row['days_to_expiry'] = days
			
			if days < 0:
				row['expiry_status'] = 'Expired'
			elif days <= 7:
				row['expiry_status'] = 'Expiring This Week'
			elif days <= 30:
				row['expiry_status'] = 'Expiring This Month'
			elif days <= 60:
				row['expiry_status'] = 'Expiring in 60 Days'
			else:
				row['expiry_status'] = 'Active'
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("expiry_status"):
		# This will be handled in post-processing
		pass
	
	if filters.get("bg_type"):
		conditions.append("bg.bg_type = %(bg_type)s")
	
	if filters.get("issuing_bank"):
		conditions.append("bg.bank = %(issuing_bank)s")
	
	# Default filter: Show BGs expiring within next 90 days
	if not filters.get("show_all"):
		conditions.append("bg.expiry_date <= DATE_ADD(CURDATE(), INTERVAL 90 DAY)")
	
	return " AND " + " AND ".join(conditions) if conditions else ""


def get_chart_data(data):
	"""Generate chart showing BG expiry distribution"""
	
	expiry_count = {
		'Expired': 0,
		'Expiring This Week': 0,
		'Expiring This Month': 0,
		'Expiring in 60 Days': 0,
		'Active': 0
	}
	
	for row in data:
		status = row.get('expiry_status', 'Active')
		if status in expiry_count:
			expiry_count[status] += 1
	
	return {
		"data": {
			"labels": list(expiry_count.keys()),
			"datasets": [
				{
					"name": "Number of BGs",
					"values": list(expiry_count.values())
				}
			]
		},
		"type": "bar",
		"colors": ["#d32f2f", "#f57c00", "#fbc02d", "#7cb342", "#388e3c"]
	}
