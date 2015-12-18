from django.db import models
from django.contrib.auth.models import User
from property_inventory.models import Property

class propertyInquiry(models.Model):
	user = models.ForeignKey(User)
	Property = models.ForeignKey(Property, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Time/Date")
	showing_scheduled = models.DateTimeField(null=True)
	applicant_ip_address = models.GenericIPAddressField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "property inquiries"
