from django.db import models
from property_inventory.models import Property

# put uploaded files in subdirectory based on address
def content_file_name(instance, filename):
	return '/'.join(['annual_reports', instance.Property.streetAddress, filename])

class annual_report(models.Model):

	parcel = models.CharField(max_length=7, blank=False, null=False)
	Property = models.ForeignKey(Property, blank=True, null=True)

	name = models.CharField(max_length=254, blank=False, null=False)
	organization = models.CharField(max_length=254, blank=True, null=True)
	email = models.EmailField(max_length=254, blank=False, null=False)
	phone = models.CharField(max_length=12, blank=False, null=False)

	percent_completed = models.PositiveIntegerField(help_text="Roughly speaking, what percentage complete is this project?")

	past_expenses = models.PositiveIntegerField(help_text="It is ok to use rough estimates.", verbose_name='Funds spent to date')
	work_completed = models.TextField(max_length=5120, help_text="What work has been completed?", verbose_name='Written narative of the improvements made to date') 

	work_remaining = models.TextField(max_length=5120, help_text="What work remains to be completed?", verbose_name='Work remaining') 
	future_expenses = models.PositiveIntegerField(help_text="It is ok to use rough estimates.", verbose_name='Anticipated remaining expenses')

	feedback = models.TextField(max_length=5120, help_text="Do you have any other comments on your project or feedback for Renew Indianapolis about your experience with our program?", verbose_name='Feedback')
	certificate_of_completion_ready = models.BooleanField(verbose_name='Are you ready for a certificate of completion inspection?', default=False)
	property_occupied = models.BooleanField(verbose_name='Is the property occupied?', default=False) 

	front_exterior_picture = models.ImageField(upload_to=content_file_name)
	back_exterior_picture = models.ImageField(upload_to=content_file_name)
	kitchen_picture = models.ImageField(upload_to=content_file_name)
	bathroom_picture = models.ImageField(upload_to=content_file_name)
	other_picture = models.ImageField(upload_to=content_file_name, blank=True, help_text='Project photo of your choice (optional)')


