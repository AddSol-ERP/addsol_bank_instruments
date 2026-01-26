# Copyright (c) 2024, Addition Solutions and contributors
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
			"label": _("LC Number"),
			"fieldtype": "Link",
			"options": "Letter of Credit",
			"width": 150
		},
		{
			"fieldname": "lc_number",
			"label": _("Bank LC Number"),
			"fieldtype": "Data",
			"width": 130
		},
		{
			"fieldname": "transaction_type",
			"label": _("Type"),
			"fieldtype": "Data",
			"width": 80
		},
		{
			"fieldname": "applicant",
			"label": _("Applicant"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "beneficiary",
			"label": _("Beneficiary"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "lc_date",
			"label": _("LC Date"),
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
			"fieldname": "lc_amount",
			"label": _("LC Amount"),
			"fieldtype": "Currency",
			"width": 120
		},
		{
			"fieldname": "balance_amount",
			"label": _("Balance Amount"),
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
			"fieldname": "issuing_bank",
			"label": _("Issuing Bank"),
			"fieldtype": "Data",
			"width": 150
		}
	]


def get_data(filters):
	conditions = get_conditions(filters)
	
	data = frappe.db.sql("""
		SELECT
			lc.name,
			lc.lc_number,
			lc.transaction_type,
			lc.applicant,
			lc.beneficiary,
			lc.lc_date,
			lc.expiry_date,
			lc.lc_amount,
			lc.balance_amount,
			lc.status,
			lc.issuing_bank
		FROM
			`tabLetter of Credit` lc
		WHERE
			lc.docstatus = 1
			AND lc.status NOT IN ('Settled', 'Cancelled')
			{conditions}
		ORDER BY
			lc.expiry_date ASC
	""".format(conditions=conditions), filters, as_dict=1)
	
	# Calculate days to expiry and expiry status
	for row in data:
		if row.expiry_date:
			days = date_diff(row.expiry_date, today())
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
	
	if filters.get("transaction_type"):
		conditions.append("lc.transaction_type = %(transaction_type)s")
	
	if filters.get("issuing_bank"):
		conditions.append("lc.issuing_bank = %(issuing_bank)s")
	
	# Default filter: Show LCs expiring within next 90 days
	if not filters.get("show_all"):
		conditions.append("lc.expiry_date <= DATE_ADD(CURDATE(), INTERVAL 90 DAY)")
	
	return " AND " + " AND ".join(conditions) if conditions else ""


def get_chart_data(data):
	"""Generate chart showing LC expiry distribution"""
	
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
					"name": "Number of LCs",
					"values": list(expiry_count.values())
				}
			]
		},
		"type": "bar",
		"colors": ["#d32f2f", "#f57c00", "#fbc02d", "#7cb342", "#388e3c"]
	}