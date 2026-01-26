import frappe
from frappe.model.document import Document

class BGManagementDocument(Document):
    pass

@frappe.whitelist()
def get_document_details(bg_name):
    """Get document details for a BG Management document"""
    documents = frappe.db.get_all("BG Management Document", 
        filters={"parent": bg_name},
        fields=["*"]
    )
    return documents
