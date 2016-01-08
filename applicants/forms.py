from django import forms
from applicants.models import Organization, ApplicantProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Button, MultiField, Field, HTML
from crispy_forms.bootstrap import FormActions
from passwords.fields import PasswordField
from localflavor.us.forms import USPhoneNumberField, USZipCodeField, USPSSelect, USStateField, USStateSelect

from .widgets import AddAnotherWidgetWrapper


class OrganizationForm(forms.ModelForm):
	phone_number = USPhoneNumberField()
	mailing_address_state = USStateField(widget=USStateSelect, required=True, label='State')
	mailing_address_zip =  USZipCodeField(required=True, label='Zipcode')

	class Meta:
		model = Organization
		exclude = ['user', 'date_created']

	def __init__(self, *args, **kwargs):
			super(OrganizationForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.form_id = 'OrganizationForm'
			self.helper.form_class = 'form-horizontal'
			#self.helper.field_class = 'col-lg-4'
			#self.helper.label_class = 'col-lg-2'
			self.helper.form_tag = True

			self.helper.layout = Layout(
				Fieldset(
					'Add Organization or Third Party',
					HTML("""
						<p>If you are applying on behalf of an organization, family member, client or other third party who will take title, provide their name and contact information.</p>
					"""),
					Field('name'),
					Field('email'),
					Field('phone_number'),
					css_class='well'
				),
				Fieldset(
					'Type and Relationship',
					Field('relationship_to_user'),
					Field('entity_type'),
					css_class='well'
				),
				Fieldset(
					'Mailing Address',
					Field('mailing_address_line1'),
					Field('mailing_address_line2'),
					Field('mailing_address_line3'),
					Field('mailing_address_city'),
					Field('mailing_address_state'),
					Field('mailing_address_zip'),
					css_class='well'
				),
				Fieldset(
					'Supporting Documents',
					HTML("""
						<p>Organizations should provide additional identifying and financial documents.</p>
					"""),
					Field('sos_business_entity_report'),
					Field('irs_determination_letter'),
					Field('most_recent_financial_statement'),
					css_class='well'
				),
	 			FormActions(
					Button('cancel', 'Cancel'),
					Submit('save', 'Save')
				)
			)
			self.helper.form_method = 'post'
			self.helper.form_action = ''


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    phone_number = USPhoneNumberField()
    mailing_address_line1 = forms.CharField(max_length='100', required=True, label='Mailing Address Line 1')
    mailing_address_line2 = forms.CharField(max_length='100', required=False, label='Mailing Address Line 2')
    mailing_address_line3 = forms.CharField(max_length='100', required=False, label='Mailing Address Line 3')
    mailing_address_city = forms.CharField(max_length='100', required=True, label='Mailing Address City')
    mailing_address_state = USStateField(widget=USStateSelect, required=True, label='Mailing Address State')
    mailing_address_zip =  USZipCodeField(required=True, label='Zipcode')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__exact=email).count() > 0:
            raise forms.ValidationError("Looks like an account with this email address already exists, did you forget your password?")
        return email


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        profile = ApplicantProfile()
        profile.phone_number = self.cleaned_data['phone_number']
        profile.mailing_address_line1 = self.cleaned_data['mailing_address_line1']
        profile.mailing_address_line2 = self.cleaned_data['mailing_address_line2']
        profile.mailing_address_line3 = self.cleaned_data['mailing_address_line3']
        profile.mailing_address_city = self.cleaned_data['mailing_address_city']
        profile.mailing_address_state = self.cleaned_data['mailing_address_state']
        profile.mailing_address_zip = self.cleaned_data['mailing_address_zip']
        profile.user = user
        profile.save()



class ApplicantProfileForm(forms.ModelForm):
	# organization = forms.ModelChoiceField(
    #     queryset=Organization.objects.all().order_by('name'),
    #     widget=AddAnotherWidgetWrapper(
    #         forms.Select(),
    #         Organization,
    #     ),
	# 	required=False
    # )
	class Meta:
		model = ApplicantProfile
		exclude = ['user']

	def __init__(self, *args, **kwargs):
			super(ApplicantProfileForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper()
			self.helper.form_id = 'ApplicantProfileForm'
			self.helper.form_class = 'form-horizontal'
			self.helper.field_class = 'col-lg-4'
			self.helper.label_class = 'col-lg-2'
			self.helper.render_unmentioned_fields = True
			self.helper.layout = Layout(
				Fieldset(
					'Add Details',
					Field('phone_number'),
					css_class='well'
				),
				Fieldset(
					'Mailing Address',
					Field('mailing_address_line1'),
					Field('mailing_address_line2'),
					Field('mailing_address_line3'),
					Field('mailing_address_city'),
					Field('mailing_address_state'),
					Field('mailing_address_zip'),
					css_class='well'
				),
				FormActions(
					Button('cancel', 'Cancel'),
					Submit('save', 'Save')
				)
			)
			self.helper.form_method = 'post'
			self.helper.form_action = ''
