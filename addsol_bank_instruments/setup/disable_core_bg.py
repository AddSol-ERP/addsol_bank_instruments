import frappe

BG_DOCTYPE = "Bank Guarantee"

def after_install():
    disable_bg_permissions()
    frappe.db.commit()

def disable_bg_permissions():
    roles = frappe.get_all("Role", pluck="name")

    for role in roles:
        if role == "System Manager":
            continue

        frappe.db.sql("""
            DELETE FROM `tabDocPerm`
            WHERE parent = %s AND role = %s
        """, (BG_DOCTYPE, role))

    frappe.clear_cache()
