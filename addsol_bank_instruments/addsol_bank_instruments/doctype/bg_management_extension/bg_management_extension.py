import frappe
from frappe.model.document import Document

class BGManagementExtension(Document):
    pass

@frappe.whitelist()
def get_extension_details(bg_name):
    """Get extension details for a BG Management document"""
    extensions = frappe.db.get_all("BG Management Extension", 
        filters={"parent": bg_name},
        fields=["*"]
    )
    return extensions
