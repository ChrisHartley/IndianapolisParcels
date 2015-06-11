from django import forms
from applicants.models import ApplicantUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Button, MultiField, Field
from crispy_forms.bootstrap import FormActions
from passwords.fields import PasswordField

class NewApplicantSignupForm(forms.ModelForm):
	password = PasswordField(label="Password")

	class Meta:
		model = ApplicantUser
		fields = ('name','email', 'organization', 'password')
		exclude = []
			
		def __init__(self, *args, **kwargs):
			super(NewApplicantSignupForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.form_id = 'NewApplicantSignupForm'
			self.helper.form_class = 'form-horizontal'
			self.helper.field_class = 'col-lg-4'
			self.helper.label_class = 'col-lg-2'
			self.helper.layout = Layout(
				Fieldset(
					'New User Signup',
					'name',
					'email',
				),
	 			FormActions(
					Button('cancel', 'Cancel'),
					Submit('save', 'Create account')
				)
			)
			self.helper.form_method = 'post'
			self.helper.form_action = ''


