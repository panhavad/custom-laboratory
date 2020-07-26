# -*- coding: utf-8 -*-
# Copyright (c) 2020, Duk Panhavad and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, cstr
from datetime import timedelta 

class Vaccination(Document):
	def on_submit(self):
		frappe.db.set_value(self.doctype,self.name,"submitted_date", getdate())
		insert_vaccination_to_medical_record(self)
		frappe.db.set_value("Vaccination", self.name, "status", "Completed")
	
	def on_cancel(self):
		delete_vaccination_from_medical_record(self)
		frappe.db.set_value("Vaccination", self.name, "status", "Cancelled")
		self.reload()

@frappe.whitelist()
def create_multiple(doctype, docname):
	vaccination_created = False
	if doctype == "Sales Invoice":
		vaccination_created = create_vaccination_from_invoice(docname)

	if vaccination_created:
		frappe.msgprint(_("Vaccination(s) {0} created".format(vaccination_created)))
	else:
		frappe.msgprint(_("No Vaccinations created"))

def create_vaccination_from_invoice(invoice_name):
	vaccination_names = list()
	vaccinations_created = False
	invoice = frappe.get_doc("Sales Invoice", invoice_name)
	if invoice.patient:
		patient = frappe.get_doc("Patient", invoice.patient)
		for item in invoice.items:
			vaccination_created = 0 
			print('-------', item.item_group)
			print('=======', item.reference_dt)
			if item.reference_dt == "Vaccination Ordered": #check if the invoice created already
				vaccination_created = 1
				vaccinations_created = "Already create before!! Cannot"
			if vaccination_created != 1:
				if item.item_group == "Vaccination":
					template = get_vaccination_template(item.item_code)
					if template:
						if template.vaccination_dosage_items:
							dosage_durations = [0]#today
							for num_day in template.vaccination_dosage_items.split('-'):
								dosage_durations.append(int(num_day))
							dosage_dates = [getdate() + timedelta(days=each_duration) for each_duration in dosage_durations]
							for dosage_number, each_dosage_date in enumerate(dosage_dates):
								vaccination = create_vaccination_doc(True, patient, template, invoice.company, each_dosage_date, dosage_number+1)
								vaccination.save(ignore_permissions = True)
								vaccinations_created = True
								vaccination_names.append(vaccination.name)
							
							if not vaccinations_created:
								vaccinations_created = vaccination.name
							else:
								vaccinations_created = ", ".join(vaccination_names)
						else:
							vaccination = create_vaccination_doc(True, patient, template, invoice.company, getdate())
							vaccination.save(ignore_permissions = True)
							vaccinations_created = vaccination.name
							
						if item.reference_dt != "Vaccination Ordered":
								frappe.db.set_value("Sales Invoice Item", item.name, "reference_dt", "Vaccination Ordered")
								frappe.db.set_value("Sales Invoice Item", item.name, "reference_dn", vaccination.name)
	return vaccinations_created

def get_vaccination_template(item):
	template_id = check_template_exists(item)
	if template_id:
		return frappe.get_doc("Vaccination Template", template_id)
	return False

def check_template_exists(item):
	template_exists = frappe.db.exists(
		"Vaccination Template",
		{
			'item': item
		}
	)
	if template_exists:
		return template_exists
	return False

def create_vaccination_doc(invoiced, patient, template, company, each_dosage_date, dosage_number):
	vaccination = frappe.new_doc("Vaccination")
	vaccination.invoiced = invoiced
	vaccination.patient = patient.name
	vaccination.patient_age = patient.get_age()
	vaccination.patient_sex = patient.sex
	vaccination.email = patient.email
	vaccination.mobile = patient.mobile
	vaccination.report_preference = patient.report_preference
	vaccination.vaccination_template = template.name
	vaccination.vaccination_name = template.name
	vaccination.dosage_date = each_dosage_date
	vaccination.dosage_number = dosage_number
	vaccination.company = company
	return vaccination

def insert_vaccination_to_medical_record(doc):
	if doc.vaccination_name:
		vac_name = frappe.bold(_("Vaccination Conducted: ")) + cstr(doc.vaccination_name) 
	else:
		vac_name = ""
	if doc.dosage_number:
		dos_number = frappe.bold(_("Dosage Number: ")) + cstr(doc.dosage_number)
	else:
		dos_number = ""
	if doc.dosage_date:
		planed_date = frappe.bold(_("Planed Dosage Date: ")) + cstr(doc.dosage_date)
	else:
		planed_date = ""
	if doc.vaccination_comment:
		comment = frappe.bold(_("Comment: ")) + cstr(doc.vaccination_comment)
	else:
		comment = ""

	actual_date = frappe.bold(_("Actual Dosage Date: ")) + cstr(getdate())
	subject = vac_name + "<br>" + dos_number + "<br>" + planed_date + "<br>" + actual_date + "<br>" + comment

	medical_record = frappe.new_doc("Patient Medical Record")
	medical_record.patient = doc.patient
	medical_record.subject = subject
	medical_record.status = "Open"
	medical_record.communication_date = getdate()
	medical_record.reference_doctype = "Vaccination"
	medical_record.reference_name = doc.name
	medical_record.reference_owner = doc.owner
	medical_record.save(ignore_permissions=True)

def delete_vaccination_from_medical_record(self):
	medical_record_id = frappe.db.sql("select name from `tabPatient Medical Record` where reference_name=%s",(self.name))

	if medical_record_id and medical_record_id[0][0]:
		frappe.delete_doc("Patient Medical Record", medical_record_id[0][0])