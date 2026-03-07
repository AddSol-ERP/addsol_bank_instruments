app_name = "addsol_bank_instruments"
app_title = "Addsol Bank Instruments"
app_publisher = "Addition Solutions"
app_description = "Management of Bank Instruments like LCs and BGs"
app_email = "erpnext@aitspl.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "addsol_bank_instruments",
# 		"logo": "/assets/addsol_bank_instruments/logo.png",
# 		"title": "Addsol Bank Instruments",
# 		"route": "/addsol_bank_instruments",
# 		"has_permission": "addsol_bank_instruments.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/addsol_bank_instruments/css/addsol_bank_instruments.css"
# app_include_js = "/assets/addsol_bank_instruments/js/addsol_bank_instruments.js"

# include js, css files in header of web template
# web_include_css = "/assets/addsol_bank_instruments/css/addsol_bank_instruments.css"
# web_include_js = "/assets/addsol_bank_instruments/js/addsol_bank_instruments.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "addsol_bank_instruments/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "addsol_bank_instruments/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "addsol_bank_instruments.utils.jinja_methods",
# 	"filters": "addsol_bank_instruments.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "addsol_bank_instruments.install.before_install"
# after_install = "addsol_bank_instruments.install.after_install"
after_install = "addsol_bank_instruments.setup.disable_core_bg.after_install"


# Uninstallation
# ------------

# before_uninstall = "addsol_bank_instruments.uninstall.before_uninstall"
# after_uninstall = "addsol_bank_instruments.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "addsol_bank_instruments.utils.before_app_install"
# after_app_install = "addsol_bank_instruments.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "addsol_bank_instruments.utils.before_app_uninstall"
# after_app_uninstall = "addsol_bank_instruments.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "addsol_bank_instruments.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# Document Events
doc_events = {
    "BG Management": {
        "validate": "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.validate_bg",
        "on_submit": "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.on_bg_submit",
        "on_cancel": "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.on_bg_cancel",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"addsol_bank_instruments.tasks.all"
# 	],
# 	"daily": [
# 		"addsol_bank_instruments.tasks.daily"
# 	],
# 	"hourly": [
# 		"addsol_bank_instruments.tasks.hourly"
# 	],
# 	"weekly": [
# 		"addsol_bank_instruments.tasks.weekly"
# 	],
# 	"monthly": [
# 		"addsol_bank_instruments.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "addsol_bank_instruments.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "addsol_bank_instruments.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "addsol_bank_instruments.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["addsol_bank_instruments.utils.before_request"]
# after_request = ["addsol_bank_instruments.utils.after_request"]

# Job Events
# ----------
# before_job = ["addsol_bank_instruments.utils.before_job"]
# after_job = ["addsol_bank_instruments.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"addsol_bank_instruments.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Notification Configuration
# Add email notifications for BG Management events

# Report Configuration
standard_queries = {
    "BG Management": "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.get_dashboard_data"
}

scheduler_events = {
    "daily": [
        "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.send_expiry_notifications",
        "addsol_bank_instruments.addsol_bank_instruments.doctype.letter_of_credit.letter_of_credit.send_lc_expiry_notifications"
    ]
}

# Permission Query Handlers
permission_query_conditions = {
    "BG Management": "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.get_permission_query_conditions",
}

has_permission = {
    "BG Management": "addsol_bank_instruments.addsol_bank_instruments.doctype.bg_management.bg_management.has_permission",
}

fixtures = [
    {
        "dt": "Workspace",
        "filters": {
            "name": "Bank Instruments"
        }
    },
    {
        "dt": "Web Page"
    }
]