from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class ApplicantProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")

	organization = models.CharField(max_length='255', null=True, blank=True)

	phone_regex = RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=16)

	mailing_address_line1 = models.CharField(max_length='100', blank=False)
	mailing_address_line2 = models.CharField(max_length='100', blank=True)
	mailing_address_line3 = models.CharField(max_length='100', blank=True)
	mailing_address_city = models.CharField(max_length='100', blank=False)
	mailing_address_state = models.CharField(max_length='100', blank=False)
	mailing_address_zip = models.CharField(max_length='100', blank=False)

	conflict_board_rc = models.BooleanField(verbose_name="Do you, any partner/member of your entity, or any of your entity's board members serve on the Renew Indianapolis Board of Directors or Committees and thus pose a potential conflict of interest?", blank=False)
	conflict_board_rc_name = models.CharField(verbose_name="If yes, what is their name?", blank=True, max_length=255)

	CURRENT_STATUS = 3
	DELINQUENT_STATUS = 2
	UNKNOWN_STATUS = 1
	NA_STATUS = None

	TAX_STATUS_CHOICES = ( (CURRENT_STATUS, 'Current'), (DELINQUENT_STATUS, 'Delinquent'), (UNKNOWN_STATUS, 'Unknown'), (NA_STATUS, 'N/A - No real property owned') )

	tax_status_of_properties_owned = models.IntegerField(
		choices=TAX_STATUS_CHOICES, 
		verbose_name='Tax status of real property owned in Marion County', 
		help_text="If you do not own any real property (real estate) in Marion County chose N/A. If you chose 'Unknown' we will contact you for an explanation"
	)

	other_properties_names_owned = models.CharField(max_length='255', verbose_name="If you own properties under other names or are a partner/member of an entity that owns properties, please list the names of those entities here")

	date_created = models.DateTimeField(auto_now_add=True)




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
