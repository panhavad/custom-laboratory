# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "custom_laboratory"
app_title = "Custom Laboratory"
app_publisher = "Duk Panhavad"
app_description = "Customisation to fit the need of small laboratory store"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "panhavadd@gmail.com"
app_license = "MIT"
fixture = ["Custom Field", "Custom Script", "Lab Test", "Lab Test Template", "Patient", "Normal Test Items"]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_laboratory/css/custom_laboratory.css"
# app_include_js = "/assets/custom_laboratory/js/custom_laboratory.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_laboratory/css/custom_laboratory.css"
# web_include_js = "/assets/custom_laboratory/js/custom_laboratory.js"

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

doctype_list_js = {
	"Vaccination":"custom_laboratory/doctype/vaccination/vaccination_list.js",
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "custom_laboratory.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "custom_laboratory.install.before_install"
# after_install = "custom_laboratory.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_laboratory.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# },
    # "Vaccination Dosage Items": {
	# 	"validate": "custom_laboratory.custom_laboratory.laboratory_custom_func.compile_vac_dosage_name"
	# }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"custom_laboratory.tasks.all"
# 	],
# 	"daily": [
# 		"custom_laboratory.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_laboratory.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_laboratory.tasks.weekly"
# 	]
# 	"monthly": [
# 		"custom_laboratory.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "custom_laboratory.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_laboratory.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "custom_laboratory.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

