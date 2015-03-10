from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class NeighborhoodAssocationSearchForm(forms.Form):
	parcel = forms.CharField(max_length=7)
	
	def __init__(self, *args, **kwargs):
		super(NeighborhoodAssocationSearchForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'propertyInquiryForm'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-8'
		self.helper.form_method = 'get'
		self.helper.form_action = ''
		self.helper.add_input(Submit('submit', 'Submit'))
