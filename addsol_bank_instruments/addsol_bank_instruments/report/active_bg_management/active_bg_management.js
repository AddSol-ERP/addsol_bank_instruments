frappe.query_reports["Active BG Management"] = {
    "filters": [
    {
        "fieldname": "company",
        "label": "Company",
        "fieldtype": "Link",
        "options": "Company",
        "default": "frappe.defaults.get_user_default('Company')"
    },
    {
        "fieldname": "from_date",
        "label": "From Date",
        "fieldtype": "Date"
    },
    {
        "fieldname": "to_date",
        "label": "To Date",
        "fieldtype": "Date"
    },
    {
        "fieldname": "bank",
        "label": "Bank",
        "fieldtype": "Link",
        "options": "Bank"
    },
    {
        "fieldname": "bg_type",
        "label": "BG Type",
        "fieldtype": "Select",
        "options": "\nPerformance Bank Guarantee\nBid Bond Guarantee\nAdvance Payment Guarantee\nRetention Money Guarantee\nFinancial Guarantee\nPayment Guarantee\nWarranty Guarantee"
    },
    {
        "fieldname": "status",
        "label": "Status",
        "fieldtype": "Select",
        "options": "\nActive\nExpired\nClaimed\nExtended\nClosed\nCancelled"
    },
    {
        "fieldname": "beneficiary",
        "label": "Beneficiary",
        "fieldtype": "Data"
    },
    {
        "fieldname": "project",
        "label": "Project",
        "fieldtype": "Link",
        "options": "Project"
    },
    {
        "fieldname": "expiring_in_days",
        "label": "Expiring in Days",
        "fieldtype": "Int",
        "description": "Show BGs expiring within specified days"
    }
]
};