from django.forms import ModelForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Button, HTML, Div, Row, Field
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions


from annual_report_form.models import annual_report


class annualReportForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(annualReportForm, self).__init__(*args, **kwargs)
		#self.fields.keyOrder = ['applicant_name','applicant_email_address','applicant_phone','parcel']
		self.helper = FormHelper()
		self.helper.form_id = 'annualReportForm'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-4'
		self.helper.form_method = 'post'
		self.helper.form_action = ''
		self.helper.layout = Layout(
			Fieldset("Property Details", 
					'parcel',
					Div(HTML('<label class="control-label col-lg-3" for="result">Street Address</label><div id="result" class="controls col-lg-4"></div>'), css_class="form-group")
					
			),
			Fieldset("Your Information",
				'name',
				'organization',
				'phone',
				'email'
			),
			Fieldset("Completed Work",
				AppendedText('percent_completed', '%', active=True),				
				PrependedText('past_expenses','$', active=False, placeholder="0.00"),
				'work_completed'

			),
			Fieldset("Remaining Work",
				PrependedText('future_expenses','$', active=True, placeholder="0.00"),
				'work_remaining',
				'certificate_of_completion_ready',
				'property_occupied'

			),
			Fieldset("Photos",
				'front_exterior_picture',
				'back_exterior_picture',
				'kitchen_picture',
				'bathroom_picture',
				'other_picture'
			),
			Fieldset("Feedback and comments",
				'feedback'
			),
			FormActions(
				Submit('save', 'Submit Report'),
				Button('cancel', 'Cancel')
			)

		)

	class Meta:
		model = annual_report
		exclude = []


