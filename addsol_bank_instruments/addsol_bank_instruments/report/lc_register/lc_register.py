# Copyright (c) 2024, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data


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
			"fieldname": "lc_type",
			"label": _("LC Type"),
			"fieldtype": "Data",
			"width": 120
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
			"fieldname": "applicant",
			"label": _("Applicant"),
			"fieldtype": "Dynamic Link",
			"options": "applicant_type",
			"width": 150
		},
		{
			"fieldname": "beneficiary",
			"label": _("Beneficiary"),
			"fieldtype": "Dynamic Link",
			"options": "beneficiary_type",
			"width": 150
		},
		{
			"fieldname": "currency",
			"label": _("Currency"),
			"fieldtype": "Link",
			"options": "Currency",
			"width": 80
		},
		{
			"fieldname": "lc_amount",
			"label": _("LC Amount"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 120
		},
		{
			"fieldname": "utilized_amount",
			"label": _("Utilized Amount"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 130
		},
		{
			"fieldname": "balance_amount",
			"label": _("Balance Amount"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 130
		},
		{
			"fieldname": "utilization_percentage",
			"label": _("Utilization %"),
			"fieldtype": "Percent",
			"width": 110
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
		},
		{
			"fieldname": "purchase_order",
			"label": _("Purchase Order"),
			"fieldtype": "Link",
			"options": "Purchase Order",
			"width": 130
		},
		{
			"fieldname": "sales_order",
			"label": _("Sales Order"),
			"fieldtype": "Link",
			"options": "Sales Order",
			"width": 130
		}
	]


def get_data(filters):
	conditions = get_conditions(filters)
	
	data = frappe.db.sql("""
		SELECT
			lc.name,
			lc.lc_number,
			lc.transaction_type,
			lc.lc_type,
			lc.lc_date,
			lc.expiry_date,
			lc.applicant,
			lc.applicant_type,
			lc.beneficiary,
			lc.beneficiary_type,
			lc.currency,
			lc.lc_amount,
			lc.utilized_amount,
			lc.balance_amount,
			CASE 
				WHEN lc.lc_amount > 0 THEN (lc.utilized_amount / lc.lc_amount) * 100
				ELSE 0
			END as utilization_percentage,
			lc.status,
			lc.issuing_bank,
			lc.purchase_order,
			lc.sales_order
		FROM
			`tabLetter of Credit` lc
		WHERE
			lc.docstatus = 1
			{conditions}
		ORDER BY
			lc.lc_date DESC
	""".format(conditions=conditions), filters, as_dict=1)
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("from_date"):
		conditions.append("lc.lc_date >= %(from_date)s")
	
	if filters.get("to_date"):
		conditions.append("lc.lc_date <= %(to_date)s")
	
	if filters.get("transaction_type"):
		conditions.append("lc.transaction_type = %(transaction_type)s")
	
	if filters.get("lc_type"):
		conditions.append("lc.lc_type = %(lc_type)s")
	
	if filters.get("status"):
		conditions.append("lc.status = %(status)s")
	
	if filters.get("currency"):
		conditions.append("lc.currency = %(currency)s")
	
	if filters.get("issuing_bank"):
		conditions.append("lc.issuing_bank = %(issuing_bank)s")
	
	if filters.get("applicant"):
		conditions.append("lc.applicant = %(applicant)s")
	
	if filters.get("beneficiary"):
		conditions.append("lc.beneficiary = %(beneficiary)s")
	
	return " AND " + " AND ".join(conditions) if conditions else ""