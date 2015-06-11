from django.db import models

class Meeting(models.Model):

    APPROVED_STATUS = 1
    NOT_APPROVED_STATUS = 2
    TABLED_STATUS = 3
	SCHEDULED_STATUS = 4

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

    STATUS_CHOICES = (
        (APPROVED_STATUS, 'Approved'),
        (NOT_APPROVED_STATUS, 'Not Approved'),
        (TABLED_STATUS, 'Tabled'),
        (SCHEDULED_STATUS, 'Scheduled'),
    )
	meeting_type = models.IntegerField(choices=MEETING_TYPE_CHOICES)
    meeting_outcome = models.IntegerField(choices=STATUS_CHOICES, null=True)
	meeting_date = models.DateField()
	application = models.ForeignKey(Application)

class UploadedFile(models.Model):
	PURPOSE_SOW = 1
	PURPOSE_POF = 2
	PURPOSE_LOS = 3
	PURPOSE_ELEVATION_VIEW = 4
	PURPOSE_SCHEDULE_OF_VALUES = 5
	PURPOSE_OTHER = 6

	FILE_PURPOSE_CHOICES(
		(PURPOSE_SOW, 'Scope of Work'),
		(PURPOSE_POF, 'Proof of Funds'),
		(PURPOSE_LOS, 'Letter of Support'),
		(PURPOSE_ELEVATION_VIEW, 'Elevation View'),
		(PURPOSE_SCHEDULE_OF_VALUES, 'Schedule of Values'),
		(PURPOSE_OTHER, 'Other'),

	)

	def return_file_path(self, filename):
		return '/'.join(['applications', self.application.id, self.application.Property.streetAddress, self.file_purpose, filename])

	models.FileField(upload_to=return_file_path)
	file_purpose = models.IntegerField(choices=FILE_PURPOSE_CHOICES)
	application = models.ForeignKey(Application)


class Application(models.Model):
	
	user = models.ForeignKey(User)
	Property = models.ForeignKey(property_inventory.property)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	HOMESTEAD = 1
	STANDARD = 2
	SIDELOT = 3

	APPLICATION_TYPES = ( 
		(HOMESTEAD, 'Homestead'), 
		(STANDARD, 'Standard'),
		(SIDELOT, 'Sidelot')
	) 

	WITHDRAWN_STATUS = 1
	HOLD_STATUS = 2
	ACTIVE_STATUS = 3
	COMPLETE_STATUS = 4

	STATUS_TYPES = ( 
		(WITHDRAWN_STATUS, 'Withdrawn'),
		(HOLD_STATUS, 'On Hold'),
		(ACTIVE_STATUS, 'Active'),
		(COMPLETE_STATUS, 'Complete') 
	) 

	application_type = models.IntegerField(
		choices=APPLICATION_TYPES, 
		verbose_name='application type', 
		help_text="If you will live in this property as your primary residence chose Homestead, otherwise chose Standard"
	)

	status = models.IntegerField(
		choices=STATUS_TYPES, 
		help_text="What is the internal status of this application?", 
		null=True
	) 

	is_rental = models.BooleanField(
		help_text="Will this property be a rental?"
	)

	planned_improvements = models.TextField(
		max_length=5120,
		help_text="Describe the improvements you plan to make to the property",
		null=False,
		blank=False
	) 

	long_term_ownership = models.CharField(
		max_length=255, 
		help_text="Who will own the property long-term?", 
		null=False, 
		blank=False
	)

	team_members = models.TextField(
		max_length=5120, 
		help_text="What contractors, property managers, construction managers, or others will be part of this work? What experience do they have?", 
		null=False, 
		blank=False
	)

	estimated_cost = models.PositiveIntegerField(
		blank=False
	)

	source_of_financing = models.TextField(
		max_length=5120, 
		help_text="What sources of financing will you use?", 
		blank=False
	)

	grant_funds = models.TextField(
		max_length=5120, 
		help_text="List grants you plan to utilize. Note whether they are committed, applied for, or planned.", 
		blank=False
	)

	timeline = models.TextField(
		max_length=5120, 
		help_text="Tell us your anticipated timeline for this project", 
		blank=False
	)

	staff_recommendation = models.BooleanField(
		help_text="Staff recommendation to Review Comittee", 
		null=True
	)

	staff_recommendation_notes = models.CharField(
		max_length=255, 
		help_text="Explanation of staff recommendation to Review Comittee", 
		null=True
	)

	staff_summary = models.TextField(
		max_length=5120,
		help_text="Staff summary of application for Review Committee",
		null=True
	)

	staff_pof_total = models.IntegerField(
		help_text="Total funds demonstrated", 
		null=True
	)

