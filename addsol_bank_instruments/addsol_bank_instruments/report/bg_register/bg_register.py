# Copyright (c) 2026, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, date_diff, today


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data


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
			"fieldname": "fd_number",
			"label": _("FD Number"),
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
		},
		{
			"fieldname": "project",
			"label": _("Project"),
			"fieldtype": "Link",
			"options": "Project",
			"width": 120
		},
		{
			"fieldname": "sales_order",
			"label": _("Sales Order"),
			"fieldtype": "Link",
			"options": "Sales Order",
			"width": 120
		},
		{
			"fieldname": "purchase_order",
			"label": _("Purchase Order"),
			"fieldtype": "Link",
			"options": "Purchase Order",
			"width": 120
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
			bg.fd_number,
			bg.fd_amount,
			bg.maturity_amount,
			bg.utilized_amount,
			bg.available_amount,
			bg.status,
			bg.bank,
			bg.project,
			bg.sales_order,
			bg.purchase_order
		FROM
			`tabBG Management` bg
		WHERE
			bg.docstatus = 1
			{conditions}
		ORDER BY
			bg.issue_date DESC
	""".format(conditions=conditions), filters, as_dict=1)
	
	# Calculate days to expiry
	for row in data:
		if row.expiry_date:
			days = date_diff(row.expiry_date, today())
			row['days_to_expiry'] = days
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("from_date"):
		conditions.append("bg.issue_date >= %(from_date)s")
	
	if filters.get("to_date"):
		conditions.append("bg.issue_date <= %(to_date)s")
	
	if filters.get("bg_type"):
		conditions.append("bg.bg_type = %(bg_type)s")
	
	if filters.get("status"):
		conditions.append("bg.status = %(status)s")
	
	if filters.get("bank"):
		conditions.append("bg.bank = %(bank)s")
	
	return " AND " + " AND ".join(conditions) if conditions else ""
