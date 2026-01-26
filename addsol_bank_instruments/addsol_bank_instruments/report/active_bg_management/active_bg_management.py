# Copyright (c) 2026, Addition Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart_data(data)
    report_summary = get_report_summary(data)
    
    return columns, data, None, chart, report_summary


def get_columns():
    return [
        {
            "label": _("BG Number"),
            "fieldname": "bg_number",
            "fieldtype": "Link",
            "options": "BG Management",
            "width": 150
        },
        {
            "label": _("Type"),
            "fieldname": "bg_type",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": _("Beneficiary"),
            "fieldname": "beneficiary_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("Issue Date"),
            "fieldname": "issue_date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("Expiry Date"),
            "fieldname": "expiry_date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("Days to Expiry"),
            "fieldname": "days_to_expiry",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": _("FD Amount"),
            "fieldname": "fd_amount",
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "label": _("Maturity Amount"),
            "fieldname": "maturity_amount",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "label": _("Utilized Amount"),
            "fieldname": "utilized_amount",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "label": _("Available Amount"),
            "fieldname": "available_amount",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "label": _("Bank"),
            "fieldname": "bank",
            "fieldtype": "Link",
            "options": "Bank",
            "width": 150
        },
        {
            "label": _("Project"),
            "fieldname": "project",
            "fieldtype": "Link",
            "options": "Project",
            "width": 150
        }
    ]


def get_data(filters):
    conditions = get_conditions(filters)
    
    data = frappe.db.sql("""
        SELECT 
            name,
            bg_number,
            bg_type,
            beneficiary_name,
            status,
            issue_date,
            CASE 
                WHEN is_extended = 1 THEN extension_expiry_date 
                ELSE expiry_date 
            END as expiry_date,
            days_to_expiry,
            fd_amount,
            maturity_amount,
            utilized_amount,
            available_amount,
            bank,
            project
        FROM `tabBG Management`
        WHERE docstatus = 1
        {conditions}
        ORDER BY 
            CASE 
                WHEN is_extended = 1 THEN extension_expiry_date 
                ELSE expiry_date 
            END ASC
    """.format(conditions=conditions), filters, as_dict=1)
    
    return data


def get_conditions(filters):
    conditions = []
    
    if filters.get("company"):
        conditions.append("applicant = %(company)s")
    
    if filters.get("bank"):
        conditions.append("bank = %(bank)s")
    
    if filters.get("bg_type"):
        conditions.append("bg_type = %(bg_type)s")
    
    if filters.get("status"):
        conditions.append("status = %(status)s")
    else:
        # Default: Show only active and extended BGs
        conditions.append("status IN ('Active', 'Extended')")
    
    if filters.get("from_date"):
        conditions.append("issue_date >= %(from_date)s")
    
    if filters.get("to_date"):
        conditions.append("issue_date <= %(to_date)s")
    
    if filters.get("beneficiary"):
        conditions.append("beneficiary = %(beneficiary)s")
    
    if filters.get("project"):
        conditions.append("project = %(project)s")
    
    # Filter by expiry within next X days
    if filters.get("expiring_in_days"):
        conditions.append("""
            DATEDIFF(
                CASE WHEN is_extended = 1 THEN extension_expiry_date ELSE expiry_date END,
                CURDATE()
            ) <= %(expiring_in_days)s
        """)
    
    return " AND " + " AND ".join(conditions) if conditions else ""


def get_chart_data(data):
    if not data:
        return None
    
    # Group by status
    status_counts = {}
    for row in data:
        status = row.get('status')
        status_counts[status] = status_counts.get(status, 0) + 1
    
    return {
        "data": {
            "labels": list(status_counts.keys()),
            "datasets": [
                {
                    "name": "Bank Guarantees",
                    "values": list(status_counts.values())
                }
            ]
        },
        "type": "donut",
        "colors": ["#29cd42", "#4C78F0", "#ffa00a", "#f44336", "#9E9E9E"]
    }


def get_report_summary(data):
    if not data:
        return []
    
    total_fd_amount = sum([d.get('fd_amount', 0) for d in data])
    total_maturity_amount = sum([d.get('maturity_amount', 0) for d in data])
    total_utilized = sum([d.get('utilized_amount', 0) for d in data])
    total_available = sum([d.get('available_amount', 0) for d in data])
    
    # Count expiring soon (within 30 days)
    expiring_soon = len([d for d in data if d.get('days_to_expiry', 999) <= 30])
    
    return [
        {
            "value": len(data),
            "indicator": "Green",
            "label": _("Total BGs"),
            "datatype": "Int"
        },
        {
            "value": total_fd_amount,
            "indicator": "Blue",
            "label": _("Total FD Amount"),
            "datatype": "Currency"
        },
        {
            "value": total_maturity_amount,
            "indicator": "Blue",
            "label": _("Total Maturity Amount"),
            "datatype": "Currency"
        },
        {
            "value": total_utilized,
            "indicator": "Orange",
            "label": _("Total Utilized"),
            "datatype": "Currency"
        },
        {
            "value": total_available,
            "indicator": "Green",
            "label": _("Total Available"),
            "datatype": "Currency"
        },
        {
            "value": expiring_soon,
            "indicator": "Red" if expiring_soon > 0 else "Green",
            "label": _("Expiring in 30 Days"),
            "datatype": "Int"
        }
    ]