from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from property_inquiry.models import propertyInquiry

class PropertyInquiryForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(PropertyInquiryForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['applicant_name','applicant_email_address','applicant_phone','parcel']
		self.helper = FormHelper()
		self.helper.form_id = 'propertyInquiryForm'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-8'
		self.helper.form_method = 'post'
		self.helper.form_action = ''
		self.helper.add_input(Submit('submit', 'Submit'))

	class Meta:
		model = propertyInquiry
		exclude = ['Property', 'showing_scheduled', 'applicant_ip_address']
