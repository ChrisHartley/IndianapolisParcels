from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField
#from applications.models import UploadedFile

class ApplicantProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")

	phone_number = PhoneNumberField()

	mailing_address_line1 = models.CharField(max_length='100', blank=False, verbose_name='Line 1')
	mailing_address_line2 = models.CharField(max_length='100', blank=True, verbose_name='Line 2')
	mailing_address_line3 = models.CharField(max_length='100', blank=True, verbose_name='Line 3')
	mailing_address_city = models.CharField(max_length='100', blank=False, verbose_name='City')
	mailing_address_state = models.CharField(max_length='100', blank=False, verbose_name='State')
	mailing_address_zip =  models.CharField(max_length='100', blank=False, verbose_name='Zipcode')

	def __unicode__(self):
		return self.user.first_name


class Organization(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(blank=False, max_length=255)

	phone_number = PhoneNumberField()

	mailing_address_line1 = models.CharField(max_length='100', blank=False, verbose_name='Line 1')
	mailing_address_line2 = models.CharField(max_length='100', blank=True, verbose_name='Line 2')
	mailing_address_line3 = models.CharField(max_length='100', blank=True, verbose_name='Line 3')
	mailing_address_city = models.CharField(max_length='100', blank=False, verbose_name='City')
	mailing_address_state = models.CharField(max_length='100', blank=False, verbose_name='State')
	mailing_address_zip =  models.CharField(max_length='100', blank=False, verbose_name='Zipcode')

	date_created = models.DateTimeField(auto_now_add=True)
	sos_business_entity_report = models.FileField(verbose_name='Secretary of State Business Entity Report', help_text='Available from the Secretary of State\'s website <a href="https://secure.in.gov/sos/online_corps/name_search.aspx">here</a>.', blank=True, null=True)
	irs_determination_letter = models.FileField(verbose_name='IRS Determination Letter', help_text='Required for 501(c)3 non-profits', blank=True, null=True)
	most_recent_financial_statement = models.FileField(verbose_name='Most Recent Financial Statement', help_text='If available', blank=True, null=True)

	def __unicode__(self):
		return self.name

#	sos_business_entity_report = models.ForeignKey('applications.UploadedFile', related_name="entity_report")
#	irs_determination_letter = models.ForeignKey('applications.UploadedFile', related_name="determination_letter")
#	most_recent_financial_statement = models.ForeignKey('applications.UploadedFile', related_name="financial_statement")

#class ApplicantUser(AbstractBaseUser, PermissionsMixin):
#	email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
#	name = models.CharField(max_length='255', null=True, blank=True)
#	organization = models.CharField(max_length='255', null=True, blank=True)
#	date_created = models.DateTimeField(auto_now_add=True)


#	#objects = AuthUserManager()
#	USERNAME_FIELD = 'email'
#	REQUIRED_FIELDS = ['name', 'password']

#	def get_full_name(self):
#		return self.name

#	def get_short_name(self):
#		return self.email

#	def __unicode__(self):
#		return self.email
