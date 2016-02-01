from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField

#from applications.models import UploadedFile


class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    phone_number = PhoneNumberField()

    mailing_address_line1 = models.CharField(
        max_length='100', blank=False, verbose_name='Line 1')
    mailing_address_line2 = models.CharField(
        max_length='100', blank=True, verbose_name='Line 2')
    mailing_address_line3 = models.CharField(
        max_length='100', blank=True, verbose_name='Line 3')
    mailing_address_city = models.CharField(
        max_length='100', blank=False, verbose_name='City')
    mailing_address_state = models.CharField(
        max_length='100', blank=False, verbose_name='State')
    mailing_address_zip = models.CharField(
        max_length='100', blank=False, verbose_name='Zipcode')

    def __unicode__(self):
        return self.user.first_name

class Organization(models.Model):

    FRIEND = 1
    FAMILY = 2
    CLIENT = 3
    EMPLOYER = 4
    OWNER = 5

    RELATIONSHIP_TYPES = (
        (FRIEND, 'Friend'),
        (FAMILY, 'Family member'),
        (CLIENT, 'Client'),
        (EMPLOYER, 'Employee'),
        (OWNER, 'Owner'),
    )

    INDIVIDUAL = 1
    NON_PROFIT_ORGANIZATION = 2
    FOR_PROFIT_ORGANIZATION = 3
    INDIVIDUAL_INVESTMENT_VEHICLE = 4

    ENTITY_TYPES = (
        (INDIVIDUAL, 'Individual'),
        (NON_PROFIT_ORGANIZATION, 'Non-profit organization'),
        (FOR_PROFIT_ORGANIZATION, 'For-profit organization (LLC, etc)'),
        (INDIVIDUAL_INVESTMENT_VEHICLE,
         'Individual Investment Vehicle (eg Self Directed IRA)'),
    )

    user = models.ForeignKey(User)
    relationship_to_user = models.IntegerField(
        choices=RELATIONSHIP_TYPES, help_text='Your relationship to this person or organization', verbose_name='Relationship to you')
    entity_type = models.IntegerField(
        choices=ENTITY_TYPES, help_text='Is this a person, corporation, investment account')

    name = models.CharField(blank=False, max_length=255)

    phone_number = PhoneNumberField(blank=True, default='')
    email = models.EmailField(blank=True, default='')

    mailing_address_line1 = models.CharField(
        max_length='100', blank=False, verbose_name='Line 1')
    mailing_address_line2 = models.CharField(
        max_length='100', blank=True, verbose_name='Line 2')
    mailing_address_line3 = models.CharField(
        max_length='100', blank=True, verbose_name='Line 3')
    mailing_address_city = models.CharField(
        max_length='100', blank=False, verbose_name='City')
    mailing_address_state = models.CharField(
        max_length='100', blank=False, verbose_name='State')
    mailing_address_zip = models.CharField(
        max_length='100', blank=False, verbose_name='Zipcode')

    date_created = models.DateTimeField(auto_now_add=True)
    # sos_business_entity_report = models.FileField(verbose_name='Secretary of State Business Entity Report',
    #                                               help_text='Available from the Secretary of State\'s website <a href="https://secure.in.gov/sos/online_corps/name_search.aspx">here</a>.', blank=True, null=True)
    # irs_determination_letter = models.FileField(
    #     verbose_name='IRS Determination Letter', help_text='Required for 501(c)3 non-profits', blank=True, null=True)
    # most_recent_financial_statement = models.FileField(
    #     verbose_name='Most Recent Financial Statement', help_text='If available', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Organization or Third Party"
        verbose_name_plural = "Organizations or Third Parties"
