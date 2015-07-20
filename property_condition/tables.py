import django_tables2 as tables2
from django_tables2_reports.tables import TableReport

from .models import ConditionReport
from property_inventory.models import Property

class ConditionReportTable(TableReport):
    #condition_avg = tables2.Column()

    class Meta:
		model = ConditionReport
		attrs = {"class": "paleblue"}
	#	exclude = {"Property"}
    #    fields = {"id", "picture", "timestamp"}
        #sequence = {}"id", "Property", "condition_avg", "timestamp", "picture", "..."}
