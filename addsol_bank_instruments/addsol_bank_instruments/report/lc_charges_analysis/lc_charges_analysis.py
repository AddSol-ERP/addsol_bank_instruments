# Copyright (c) 2024, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart_data(data)
	summary = get_summary(data)
	return columns, data, None, chart, summary


def get_columns():
	return [
		{
			"fieldname": "lc_name",
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
			"fieldname": "charge_type",
			"label": _("Charge Type"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "charge_date",
			"label": _("Charge Date"),
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "currency",
			"label": _("Currency"),
			"fieldtype": "Link",
			"options": "Currency",
			"width": 80
		},
		{
			"fieldname": "amount",
			"label": _("Amount"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 120
		},
		{
			"fieldname": "payment_entry",
			"label": _("Payment Entry"),
			"fieldtype": "Link",
			"options": "Payment Entry",
			"width": 150
		},
		{
			"fieldname": "journal_entry",
			"label": _("Journal Entry"),
			"fieldtype": "Link",
			"options": "Journal Entry",
			"width": 150
		},
		{
			"fieldname": "beneficiary",
			"label": _("Beneficiary"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "issuing_bank",
			"label": _("Issuing Bank"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "remarks",
			"label": _("Remarks"),
			"fieldtype": "Small Text",
			"width": 200
		}
	]


def get_data(filters):
	conditions = get_conditions(filters)
	
	data = frappe.db.sql("""
		SELECT
			lc.name as lc_name,
			lc.lc_number,
			lc.transaction_type,
			lc.beneficiary,
			lc.issuing_bank,
			charge.charge_type,
			charge.charge_date,
			charge.currency,
			charge.amount,
			charge.payment_entry,
			charge.journal_entry,
			charge.remarks
		FROM
			`tabLetter of Credit` lc
		INNER JOIN
			`tabLC Charges` charge ON charge.parent = lc.name
		WHERE
			lc.docstatus = 1
			{conditions}
		ORDER BY
			charge.charge_date DESC, lc.name
	""".format(conditions=conditions), filters, as_dict=1)
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("from_date"):
		conditions.append("charge.charge_date >= %(from_date)s")
	
	if filters.get("to_date"):
		conditions.append("charge.charge_date <= %(to_date)s")
	
	if filters.get("transaction_type"):
		conditions.append("lc.transaction_type = %(transaction_type)s")
	
	if filters.get("charge_type"):
		conditions.append("charge.charge_type = %(charge_type)s")
	
	if filters.get("currency"):
		conditions.append("charge.currency = %(currency)s")
	
	if filters.get("issuing_bank"):
		conditions.append("lc.issuing_bank = %(issuing_bank)s")
	
	if filters.get("lc_number"):
		conditions.append("lc.name = %(lc_number)s")
	
	return " AND " + " AND ".join(conditions) if conditions else ""


def get_chart_data(data):
	"""Generate chart showing charge type distribution"""
	
	charge_totals = {}
	
	for row in data:
		charge_type = row.get('charge_type', 'Other')
		amount = row.get('amount', 0)
		
		if charge_type in charge_totals:
			charge_totals[charge_type] += amount
		else:
			charge_totals[charge_type] = amount
	
	# Sort by amount descending
	sorted_charges = sorted(charge_totals.items(), key=lambda x: x[1], reverse=True)
	
	return {
		"data": {
			"labels": [item[0] for item in sorted_charges],
			"datasets": [
				{
					"name": "Total Amount",
					"values": [item[1] for item in sorted_charges]
				}
			]
		},
		"type": "bar"
	}


def get_summary(data):
	"""Generate summary cards"""
	
	total_charges = sum([row.amount for row in data])
	unique_lcs = len(set([row.lc_name for row in data]))
	avg_charge_per_lc = total_charges / unique_lcs if unique_lcs > 0 else 0
	
	# Count by charge type
	charge_types = {}
	for row in data:
		charge_type = row.get('charge_type', 'Other')
		if charge_type in charge_types:
			charge_types[charge_type] += 1
		else:
			charge_types[charge_type] = 1
	
	most_common_charge = max(charge_types.items(), key=lambda x: x[1])[0] if charge_types else "N/A"
	
	return [
		{
			"value": len(data),
			"label": "Total Charge Entries",
			"datatype": "Int",
			"indicator": "blue"
		},
		{
			"value": total_charges,
			"label": "Total Charges Amount",
			"datatype": "Currency",
			"indicator": "red"
		},
		{
			"value": unique_lcs,
			"label": "LCs with Charges",
			"datatype": "Int",
			"indicator": "blue"
		},
		{
			"value": avg_charge_per_lc,
			"label": "Avg Charge per LC",
			"datatype": "Currency",
			"indicator": "orange"
		},
		{
			"value": most_common_charge,
			"label": "Most Common Charge",
			"datatype": "Data",
			"indicator": "green"
		}
	]