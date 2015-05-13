from django_tables2_reports.tables import TableReport

from property_inventory.models import Property

class PropertyStatusTable(TableReport):
	class Meta:
		model = Property
		attrs = {"class": "paleblue"}
		fields = ("parcel", "streetAddress", "zipcode", "structureType", "applicant", "status", )


class PropertySearchTable(TableReport):
	class Meta:
		model = Property
		attrs = {"class": "paleblue", "id": "myTable"}
		fields = ("parcel", "streetAddress", "zipcode", "structureType", "cdc", "zoning", "nsp", "quiet_title_complete", "side_lot_eligible", "area", "status", "bep_demolition", "urban_garden", "price" )
