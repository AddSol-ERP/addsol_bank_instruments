import frappe

def get_notification_config():
    """
    Returns notification configuration for Bank Instruments app.
    This function is called by Frappe's notification system.
    """
    return {
        "for_doctype": {
            "BG Management": {
                "subject": "{{ doc.name }} - {{ doc.status }}",
                "message": "Bank Guarantee {{ doc.name }} has been {{ doc.status }}",
                "condition": "doc.status in ['Active', 'Cancelled', 'Claimed', 'Extended', 'Closed', 'Expired']"
            },
            "Letter of Credit": {
                "subject": "{{ doc.name }} - {{ doc.status }}",
                "message": "Letter of Credit {{ doc.name }} has been {{ doc.status }}",
                "condition": "doc.status in ['Opened', 'Amended', 'Documents Submitted', 'Documents Accepted', 'Payment Made', 'Settled', 'Cancelled', 'Expired']"
            }
        }
    }
