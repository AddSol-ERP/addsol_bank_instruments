# Copyright (c) 2026, Addition Solutions and contributors
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
			"fieldname": "beneficiary_name",
			"label": _("Beneficiary"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "fd_amount",
			"label": _("FD Amount"),
			"fieldtype": "Currency",
			"width": 120
		},
		{
			"fieldname": "commission_rate",
			"label": _("Commission Rate %"),
			"fieldtype": "Percent",
			"width": 120
		},
		{
			"fieldname": "commission_amount",
			"label": _("Commission Amount"),
			"fieldtype": "Currency",
			"width": 130
		},
		{
			"fieldname": "processing_charges",
			"label": _("Processing Charges"),
			"fieldtype": "Currency",
			"width": 130
		},
		{
			"fieldname": "total_charges",
			"label": _("Total Charges"),
			"fieldtype": "Currency",
			"width": 120
		},
		{
			"fieldname": "charges_percentage",
			"label": _("Charges % of FD"),
			"fieldtype": "Percent",
			"width": 120
		},
		{
			"fieldname": "bank",
			"label": _("Issuing Bank"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "issue_date",
			"label": _("Issue Date"),
			"fieldtype": "Date",
			"width": 100
		}
	]


def get_data(filters):
	conditions = get_conditions(filters)
	
	data = frappe.db.sql("""
		SELECT
			bg.name,
			bg.bg_type,
			bg.beneficiary_name,
			bg.fd_amount,
			bg.commission_rate,
			bg.commission_amount,
			bg.processing_charges,
			bg.total_charges,
			bg.bank,
			bg.issue_date
		FROM
			`tabBG Management` bg
		WHERE
			bg.docstatus = 1
			{conditions}
		ORDER BY
			bg.issue_date DESC
	""".format(conditions=conditions), filters, as_dict=1)
	
	# Calculate charges percentage
	for row in data:
		if row.fd_amount > 0:
			row['charges_percentage'] = (row.total_charges / row.fd_amount) * 100
		else:
			row['charges_percentage'] = 0
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("from_date"):
		conditions.append("bg.issue_date >= %(from_date)s")
	
	if filters.get("to_date"):
		conditions.append("bg.issue_date <= %(to_date)s")
	
	if filters.get("bg_type"):
		conditions.append("bg.bg_type = %(bg_type)s")
	
	if filters.get("bank"):
		conditions.append("bg.bank = %(bank)s")
	
	return " AND " + " AND ".join(conditions) if conditions else ""


def get_chart_data(data):
	"""Generate chart showing charges distribution by BG type"""
	
	charges_by_type = {}
	for row in data:
		bg_type = row.get('bg_type', 'Unknown')
		if bg_type not in charges_by_type:
			charges_by_type[bg_type] = 0
		charges_by_type[bg_type] += row.get('total_charges', 0)
	
	return {
		"data": {
			"labels": list(charges_by_type.keys()),
			"datasets": [
				{
					"name": "Total Charges",
					"values": list(charges_by_type.values())
				}
			]
		},
		"type": "pie",
		"colors": ["#388e3c", "#f57c00", "#d32f2f", "#7cb342", "#fbc02d", "#ff9800", "#9e9e9e"]
	}


def get_summary(data):
	"""Generate summary cards"""
	
	total_fd_amount = sum([row.fd_amount for row in data])
	total_commission = sum([row.commission_amount for row in data])
	total_processing = sum([row.processing_charges for row in data])
	total_charges = sum([row.total_charges for row in data])
	
	avg_charges_percentage = (total_charges / total_fd_amount * 100) if total_fd_amount > 0 else 0
	
	return [
		{
			"value": len(data),
			"label": "Total BGs",
			"datatype": "Int",
			"indicator": "blue"
		},
		{
			"value": total_fd_amount,
			"label": "Total FD Amount",
			"datatype": "Currency",
			"indicator": "blue"
		},
		{
			"value": total_commission,
			"label": "Total Commission",
			"datatype": "Currency",
			"indicator": "green"
		},
		{
			"value": total_processing,
			"label": "Total Processing Charges",
			"datatype": "Currency",
			"indicator": "orange"
		},
		{
			"value": total_charges,
			"label": "Total Charges",
			"datatype": "Currency",
			"indicator": "red"
		},
		{
			"value": avg_charges_percentage,
			"label": "Avg Charges %",
			"datatype": "Percent",
			"indicator": "purple"
		}
	]
