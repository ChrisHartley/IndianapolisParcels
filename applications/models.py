from django.db import models
from django.contrib.auth.models import User

from property_inventory.models import Property
from applicants.models import Organization
from neighborhood_associations.models import Neighborhood_Association
from django.utils.deconstruct import deconstructible



from django.conf import settings



@deconstructible
class UploadToApplicationDir(object):
    path = "applicants/{0}/{1}{2}"

    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return "applicants/{0}/{1}{2}".format(instance.user.email, self.sub_path, filename)


class Application(models.Model):

    user = models.ForeignKey(User)
    Property = models.ForeignKey(Property, null=True, blank=True)
    organization = models.ForeignKey(Organization, null=True, blank=True,
                                     help_text="This is the name that will be shown on the deed, if ")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    HOMESTEAD = 1
    STANDARD = 2
    SIDELOT = 3

    APPLICATION_TYPES = (
        (HOMESTEAD, 'Homestead - this will be your primary residence'),
        (STANDARD, 'Standard - property will be sold or rented, or is non-residential'),
        (SIDELOT, 'Sidelot - vacant lot adjacent to your primary residence')
    )

    WITHDRAWN_STATUS = 1
    HOLD_STATUS = 2
    ACTIVE_STATUS = 3
    COMPLETE_STATUS = 4
    INITIAL_STATUS = 5

    STATUS_TYPES = (
        (WITHDRAWN_STATUS, 'Withdrawn'),
        (HOLD_STATUS, 'On Hold'),
        (ACTIVE_STATUS, 'Active / In Progress'),
        (COMPLETE_STATUS, 'Complete / Submitted'),
        (INITIAL_STATUS, 'Initial state'),
    )

    YES_CHOICE = True
    NO_CHOICE = False
    YESNO_TYPES = (
        (YES_CHOICE, 'Yes'),
        (NO_CHOICE, 'No')
    )

    CURRENT_STATUS = 3
    DELINQUENT_STATUS = 2
    UNKNOWN_STATUS = 1
    NA_STATUS = 0

    TAX_STATUS_CHOICES = (
        (CURRENT_STATUS, 'Current'),
        (DELINQUENT_STATUS, 'Delinquent'),
        (UNKNOWN_STATUS, 'Unknown'),
        (NA_STATUS, 'N/A - No property owned')
    )

    application_type = models.IntegerField(
        choices=APPLICATION_TYPES,
        verbose_name='Application Type',
        null=True,
        blank=True,
        help_text="If you will live in this property as your primary residence chose Homestead, if you will rent or sell chose Standard. If this is a side lot adjacent to your primary residence chose Sidelot."
    )

    status = models.IntegerField(
        choices=STATUS_TYPES,
        help_text="What is the internal status of this application?",
        null=False,
        default=INITIAL_STATUS,
        verbose_name='Status'
    )

    is_rental = models.NullBooleanField(
        choices=YESNO_TYPES,
        verbose_name='Rental Property',
        help_text="Will this property be a rental?"
    )

    planned_improvements = models.TextField(
        max_length=5120,
        help_text="Tell us about your plans for this property and who will do what work.",
        blank=True
    )

    long_term_ownership = models.CharField(
        max_length=255,
        help_text="Who will own the property long-term?",
        blank=True
    )

    estimated_cost = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="How much do you estimate your project will cost?"
    )

    source_of_financing = models.TextField(
        max_length=5120,
        help_text="""
			Tell us how you plan to pay for the proposed improvements, including any donated materials or
			labor from friends and family.  Also include any grants you plan to apply for, including the
			name of the grant and whether it is awarded, pending, or not yet submitted.
		""",
        blank=True
    )

    timeline = models.TextField(
        max_length=5120,
        help_text="Tell us your anticipated timeline for this project. You can take up to 24 months from closing to complete the work in your scope of work.",
        blank=True
    )

    staff_recommendation = models.NullBooleanField(
        help_text="Staff recommendation to Review Comittee",
        null=True
    )

    staff_recommendation_notes = models.CharField(
        max_length=255,
        help_text="Explanation of staff recommendation to Review Comittee",
        blank=True
    )

    staff_summary = models.TextField(
        max_length=5120,
        help_text="Staff summary of application for Review Committee",
        blank=True
    )

    staff_pof_total = models.DecimalField(max_digits=10, decimal_places=2,
        help_text="Total funds demonstrated",
        verbose_name='Staff determined PoF',
        null=True,
        blank=True
    )

    staff_pof_description = models.CharField(max_length=1024, blank=True, verbose_name="Staff description of proof of funds provided")

    staff_points_to_consider = models.CharField(
        verbose_name="Staff's suggested points to consider",
        max_length=255,
        blank=True
    )

    # neighborhood notification - boolean or file? boolean and then collection
    # of files

    conflict_board_rc = models.NullBooleanField(
        choices=YESNO_TYPES,
        verbose_name="Do you, any partner/member of your entity, or any of your entity's board members serve on the Renew Indianapolis Board of Directors or Committees and thus pose a potential conflict of interest?",
        blank=True
    )

    conflict_board_rc_name = models.CharField(
        verbose_name="If yes, what is his or her name?",
        blank=True,
        max_length=255
    )

    active_citations = models.NullBooleanField(
        choices=YESNO_TYPES,
        verbose_name="Do you own any property that is subject to any un-remediated citation of violation of the state and local codes and ordinances?",
        help_text="The unsafe building code and building code history of properties owned by the prospective buyer, or by individuals or entities related to the prospective buyer, will be a factor in determining eligibility.  Repeat violations, unmitigated violations, and unpaid civil penalties may cause a buyer to be ineligible",
        blank=True
    )

    tax_status_of_properties_owned = models.IntegerField(
        choices=TAX_STATUS_CHOICES,
        null=True,
        blank=True,
        verbose_name='Tax status of property currently owned in Marion County',
        help_text="If you do not own any property (real estate) in Marion County chose N/A. If you chose 'Unknown' we will contact you for an explanation.",
    )

    other_properties_names_owned = models.CharField(
        max_length='255',
        verbose_name="If you own properties under other names or are a partner/member of an entity that owns properties, please list the names of those entities here",
        blank=True
    )

    prior_tax_foreclosure = models.NullBooleanField(
        choices=YESNO_TYPES,
        verbose_name="Were you the prior owner of any property in Marion County that was transferred to the Treasurer or to a local government as a result of tax foreclosure proceedings?",
        blank=True
    )

    sidelot_eligible = models.NullBooleanField(
        choices=YESNO_TYPES,
        verbose_name='Do you qualify for our side lot program?',
        help_text='To be eligible for our side lot program you must claim a homestead deduction on an adjacent property that shares at least a 75% property line with the vacant lot you are applying for. If you are not eligible you may still apply but you will be required to complete a sidelot policy waiver form, which we will email to you.'
    )

    nsp_income_qualifier = models.CharField(
        max_length='255',
        verbose_name="Which entity will conduct the income qualification process for new tenants for this property?",
        help_text="Federal policies require that during the affordability period (5 years from your purchase), tenants must be at or below 80% of the Area Median Income. Verifying tenant income is a complicated process that must be completed by a qualified entity with experience in this field.  If your organization will do this itself, enter 'self'.",
        blank=True
    )

    frozen = models.BooleanField(
        default=False,
        verbose_name='Freeze Application for Review',
        help_text="Frozen applications are ready for review and can not be edited by the applicant"
    )

    def __unicode__(self):
        if self.organization:
            return '%s - %s - %s' % (self.user.email, self.organization.name, self.Property)
        return '%s - %s' % (self.user.email, self.Property)

class NeighborhoodNotification(models.Model):
    application = models.ForeignKey(Application, related_name="notification")
    neighborhood = models.ForeignKey(Neighborhood_Association, blank=True)
    #neighborhood = models.CharField(blank=True, max_length=1024)
    #neighborhood = models.IntegerField(blank=True)
    feedback = models.CharField(blank=True, max_length=1024)

class Meeting(models.Model):
    REVIEW_COMMITTEE = 1
    BOARD_OF_DIRECTORS = 2
    MDC = 3
    RFP_COMMITTEE = 4

    MEETING_TYPE_CHOICES = (
        (REVIEW_COMMITTEE, 'Review Committee'),
        (BOARD_OF_DIRECTORS, 'Board of Directors'),
        (MDC, 'Metropolitan Development Commission'),
        (RFP_COMMITTEE, 'RFP Committee'),
    )

    meeting_date = models.DateField()
    meeting_type = models.IntegerField(choices=MEETING_TYPE_CHOICES)

    def __unicode__(self):
        return '%s - %s' % (self.get_meeting_type_display(), self.meeting_date)


class MeetingLink(models.Model):

    APPROVED_STATUS = 1
    NOT_APPROVED_STATUS = 2
    TABLED_STATUS = 3
    SCHEDULED_STATUS = 4

    STATUS_CHOICES = (
        (APPROVED_STATUS, 'Approved'),
        (NOT_APPROVED_STATUS, 'Not Approved'),
        (TABLED_STATUS, 'Tabled'),
        (SCHEDULED_STATUS, 'Scheduled'),
    )
    meeting = models.ForeignKey(Meeting, related_name='meeting_link')
    meeting_outcome = models.IntegerField(choices=STATUS_CHOICES, null=False, default=SCHEDULED_STATUS)
    application = models.ForeignKey(Application, related_name='meeting')
    notes = models.CharField(max_length=1024, blank=True, null=False)

    @property
    def meeting_date(self):
        return self.meeting.meeting_date

    def __unicode__(self):
        return '%s - %s' % (self.meeting, self.get_meeting_outcome_display())

    class Meta:
        get_latest_by = 'meeting_date'
