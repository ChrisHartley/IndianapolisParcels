import django_tables2 as tables2
from django_tables2_reports.tables import TableReport

from property_inquiry.models import propertyInquiry
from property_inventory.models import Property

class PropertyInquiryTable(TableReport):

	Property = tables2.Column()
	#parcel = tables2.Column(accessor='Property.parcel')
	#street_address = tables2.Column(accessor='Property.streetAddress')
	inquiry_count = tables2.Column(empty_values=(), orderable=False)
	inquirier_count = tables2.Column(empty_values=(), orderable=False)
	current_status = tables2.Column(accessor='Property.status')
	user = tables2.Column(accessor='user.email')
	user_name = tables2.Column(empty_values=())

	def render_user_name(self, record):
		return record.user.first_name + ' ' + record.user.last_name

	def render_street_address(self, record):
		return record.Property.streetAddress

	def render_inquiry_count(self, record):
		return	propertyInquiry.objects.filter(Property__exact=record.Property).count()

	def render_inquirier_count(self, record):
		return	propertyInquiry.objects.filter(user=record.user).count()

	class Meta:
		model = propertyInquiry
		attrs = {"class": "paleblue"}
		#exclude = {"Property"}
		sequence = ("id", "Property", "inquiry_count", "user", "user_name", "...")
