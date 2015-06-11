import django_tables2 as tables2
from django_tables2_reports.tables import TableReport

from .models import annual_report

class AnnualReportTable(TableReport):
	id_number = tables2.TemplateColumn('<a href="{% url \'annual_report_form.views.showAnnualReportData\' id=record.id %}">{{record.id}}</a>')
	class Meta:
		model = annual_report
		attrs = {"class": "paleblue"}
		fields = ("id_number",  "Property", "name", "organization", "email", "phone", "percent_completed")
