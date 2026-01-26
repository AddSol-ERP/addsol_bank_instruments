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
			"fieldname": "claim_count",
			"label": ("Claims"),
			"fieldtype": "Int",
			"width": 90
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
			bg.beneficiary_name,
			bg.issue_date,
			bg.expiry_date,
			bg.fd_amount,
			bg.maturity_amount,
			bg.utilized_amount,
			bg.available_amount,
			bg.status,
			bg.bank,
			(SELECT COUNT(*) FROM `tabBG Management Extension` WHERE parent = bg.name) as extension_count
		FROM
			`tabBG Management` bg
		WHERE
			bg.docstatus = 1
			{conditions}
		ORDER BY
			bg.issue_date DESC
	""".format(conditions=conditions), filters, as_dict=1)
	
	# Calculate derived fields
	for row in data:
		# Calculate utilization percentage
		if row.maturity_amount > 0:
			row['utilization_percentage'] = (row.utilized_amount / row.maturity_amount) * 100
		else:
			row['utilization_percentage'] = 0
		
		# Determine utilization status
		if row.utilized_amount == 0:
			row['utilization_status'] = 'Not Utilized'
		elif row.utilized_amount >= row.maturity_amount:
			row['utilization_status'] = 'Fully Utilized'
		elif row.utilization_percentage >= 75:
			row['utilization_status'] = 'Highly Utilized'
		elif row.utilization_percentage >= 50:
			row['utilization_status'] = 'Moderately Utilized'
		else:
			row['utilization_status'] = 'Low Utilization'
		
		# Count claims (assuming claim_date indicates a claim)
		row['claim_count'] = 1 if row.claim_date else 0
	
	return data


def get_conditions(filters):
	conditions = []
	
	if filters.get("from_date"):
		conditions.append("bg.issue_date >= %(from_date)s")
	
	if filters.get("to_date"):
		conditions.append("bg.issue_date <= %(to_date)s")
	
	if filters.get("bg_type"):
		conditions.append("bg.bg_type = %(bg_type)s")
	
	if filters.get("currency"):
		# Assuming currency is stored in a separate field or derived from company
		conditions.append("1=0")  # Placeholder - adjust based on actual currency field
	
	if filters.get("utilization_status"):
		# Will be filtered in post-processing
		pass
	
	if filters.get("status"):
		conditions.append("bg.status = %(status)s")
	
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
					"name": "Number of BGs",
					"values": list(utilization_count.values())
				}
			]
		},
		"type": "bar",
		"colors": ["#9e9e9e", "#fbc02d", "#ff9800", "#f57c00", "#388e3c"]
	}


def get_summary(data):
	"""Generate summary cards"""
	
	total_fd_amount = sum([row.fd_amount for row in data])
	total_maturity_amount = sum([row.maturity_amount for row in data])
	total_utilized = sum([row.utilized_amount for row in data])
	total_available = sum([row.available_amount for row in data])
	
	avg_utilization = (total_utilized / total_maturity_amount * 100) if total_maturity_amount > 0 else 0
	
	return [
		{
			"value": len(data),
			"label": "Total BGs",
			"datatype": "Int",
			"indicator": "blue"
		},
		{
			"value": total_maturity_amount,
			"label": "Total Maturity Amount",
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
			"value": total_available,
			"label": "Total Available",
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
