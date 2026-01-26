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
			"fieldname": "beneficiary",
			"label": _("Beneficiary"),
			"fieldtype": "Data",
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
			"fieldname": "tolerance_percentage",
			"label": _("Tolerance %"),
			"fieldtype": "Percent",
			"width": 100
		},
		{
			"fieldname": "max_lc_amount",
			"label": _("Max Amount (With Tolerance)"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 180
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
			"fieldname": "utilization_status",
			"label": _("Utilization Status"),
			"fieldtype": "Data",
			"width": 130
		},
		{
			"fieldname": "shipment_count",
			"label": _("Shipments"),
			"fieldtype": "Int",
			"width": 90
		},
		{
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Data",
			"width": 120
		}
	]


def get_data(filters):
	conditions = get_conditions(filters)
	
	data = frappe.db.sql("""
		SELECT
			lc.name,
			lc.lc_number,
			lc.transaction_type,
			lc.beneficiary,
			lc.currency,
			lc.lc_amount,
			lc.tolerance_percentage,
			lc.utilized_amount,
			lc.balance_amount,
			lc.status,
			(SELECT COUNT(*) FROM `tabLC Shipment` WHERE parent = lc.name) as shipment_count
		FROM
			`tabLetter of Credit` lc
		WHERE
			lc.docstatus = 1
			{conditions}
		ORDER BY
			lc.lc_date DESC
	""".format(conditions=conditions), filters, as_dict=1)
	
	# Calculate derived fields
	for row in data:
		# Calculate max LC amount with tolerance
		tolerance_amount = (row.lc_amount * row.tolerance_percentage) / 100
		row['max_lc_amount'] = row.lc_amount + tolerance_amount
		
		# Calculate utilization percentage
		if row.lc_amount > 0:
			row['utilization_percentage'] = (row.utilized_amount / row.lc_amount) * 100
		else:
			row['utilization_percentage'] = 0
		
		# Determine utilization status
		if row.utilized_amount == 0:
			row['utilization_status'] = 'Not Utilized'
		elif row.utilized_amount >= row.max_lc_amount:
			row['utilization_status'] = 'Fully Utilized'
		elif row.utilization_percentage >= 75:
			row['utilization_status'] = 'Highly Utilized'
		elif row.utilization_percentage >= 50:
			row['utilization_status'] = 'Moderately Utilized'
		else:
			row['utilization_status'] = 'Low Utilization'
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("from_date"):
		conditions.append("lc.lc_date >= %(from_date)s")
	
	if filters.get("to_date"):
		conditions.append("lc.lc_date <= %(to_date)s")
	
	if filters.get("transaction_type"):
		conditions.append("lc.transaction_type = %(transaction_type)s")
	
	if filters.get("currency"):
		conditions.append("lc.currency = %(currency)s")
	
	if filters.get("utilization_status"):
		# Will be filtered in post-processing
		pass
	
	if filters.get("status"):
		conditions.append("lc.status = %(status)s")
	
	return " AND " + " AND ".join(conditions) if conditions else ""


def get_chart_data(data):
	"""Generate chart showing utilization distribution"""
	
	utilization_count = {
		'Not Utilized': 0,
		'Low Utilization': 0,
		'Moderately Utilized': 0,
		'Highly Utilized': 0,
		'Fully Utilized': 0
	}
	
	for row in data:
		status = row.get('utilization_status', 'Not Utilized')
		if status in utilization_count:
			utilization_count[status] += 1
	
	return {
		"data": {
			"labels": list(utilization_count.keys()),
			"datasets": [
				{
					"name": "Number of LCs",
					"values": list(utilization_count.values())
				}
			]
		},
		"type": "bar",
		"colors": ["#9e9e9e", "#fbc02d", "#ff9800", "#f57c00", "#388e3c"]
	}


def get_summary(data):
	"""Generate summary cards"""
	
	total_lc_amount = sum([row.lc_amount for row in data])
	total_utilized = sum([row.utilized_amount for row in data])
	total_balance = sum([row.balance_amount for row in data])
	
	avg_utilization = (total_utilized / total_lc_amount * 100) if total_lc_amount > 0 else 0
	
	return [
		{
			"value": len(data),
			"label": "Total LCs",
			"datatype": "Int",
			"indicator": "blue"
		},
		{
			"value": total_lc_amount,
			"label": "Total LC Amount",
			"datatype": "Currency",
			"indicator": "blue"
		},
		{
			"value": total_utilized,
			"label": "Total Utilized",
			"datatype": "Currency",
			"indicator": "green"
		},
		{
			"value": total_balance,
			"label": "Total Balance",
			"datatype": "Currency",
			"indicator": "orange"
		},
		{
			"value": avg_utilization,
			"label": "Avg Utilization %",
			"datatype": "Percent",
			"indicator": "green"
		}
	]