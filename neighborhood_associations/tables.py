from django_tables2_reports.tables import TableReport
from neighborhood_associations.models import Neighborhood_Association

class NeighborhoodAssociationTable(TableReport):

	class Meta:
		model = Neighborhood_Association
		attrs = {"class": "paleblue"}
		exclude = {"geometry"}
		fields = ("name", "contact_first_name", "contact_last_name", "contact_email_address", "last_updated", "area2" )

