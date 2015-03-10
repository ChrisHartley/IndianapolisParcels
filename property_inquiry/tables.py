import django_tables2 as tables2
from django_tables2_reports.tables import TableReport

from property_inquiry.models import propertyInquiry
from property_inventory.models import Property

class PropertyInquiryTable(TableReport):

	#Property__parcel = tables2.Column()
	#street_address = tables2.Column(empty_values=())
	street_address = tables2.Column(accessor='Property.streetAddress')
	inquiry_count = tables2.Column(empty_values=(), orderable=False)
	inquirier_count = tables2.Column(empty_values=(), orderable=False)
	current_status = tables2.Column(accessor='Property.status')

	def render_street_address(self, record):
		return Property.objects.get(parcel__exact=record.parcel).streetAddress

	def render_inquiry_count(self, record):
		return	propertyInquiry.objects.filter(parcel__exact=record.parcel).count()

	def render_inquirier_count(self, record):
		return	propertyInquiry.objects.filter(applicant_email_address__exact=record.applicant_email_address).count()

	class Meta:
		model = propertyInquiry
		attrs = {"class": "paleblue"}
		exclude = {"Property"}
		sequence = ("id", "street_address", "parcel", "inquiry_count", "...")
