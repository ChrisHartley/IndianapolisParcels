from django_tables2_reports.tables import TableReport

from property_inventory.models import Property

class PropertyStatusTable(TableReport):
	class Meta:
		model = Property
		attrs = {"class": "paleblue"}
		fields = ("parcel", "streetAddress", "zipcode", "structureType", "applicant", "status", )
