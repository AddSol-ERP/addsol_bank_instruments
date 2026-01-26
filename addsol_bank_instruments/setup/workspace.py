import frappe

def hide_bg_from_workspace():
    workspaces = frappe.get_all("Workspace", pluck="name")

    for ws in workspaces:
        doc = frappe.get_doc("Workspace", ws)
        if not doc.content:
            continue

        if "Bank Guarantee" in doc.content:
            doc.content = doc.content.replace("Bank Guarantee", "")
            doc.save(ignore_permissions=True)

    frappe.db.commit()
