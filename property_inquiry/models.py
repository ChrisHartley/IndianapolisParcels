from django.db import models
from property_inventory.models import Property

# Create your models here.
class propertyInquiry(models.Model):
	parcel = models.CharField(max_length=7, blank=False, null=False)
	applicant_name = models.CharField(max_length=255, blank=False, null=False)
	applicant_email_address = models.EmailField(blank=False, null=False)
	applicant_phone = models.CharField(max_length=15, blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	Property = models.ForeignKey(Property, blank=True, null=True)
	showing_scheduled = models.DateTimeField(null=True)
	applicant_ip_address = models.GenericIPAddressField(blank=True, null=True)


	def clean(self):
		try: 
			structureType = Property.objects.get(parcel=self.parcel).structureType
			status = Property.objects.get(parcel=self.parcel).status
		except Property.DoesNotExist:
			raise ValidationError('That parcel is not in our inventory')
		if structureType == 'Vacant Lot':
			raise ValidationError('Our records show this is a vacant lot and so you can not submit a property inquiry. If our data are incorrect, please email us at chris.hartley@renewindianapolis.org so we can correct our data and set up a showing.')
		if (status == 'Sold' or 'Sale approved by MDC' in status):
			raise ValidationError('This parcel has been sold or is approved for sale and is no longer available from Renew Indianapolis.')	
	
	class Meta:
		verbose_name_plural = "property inquiries"
