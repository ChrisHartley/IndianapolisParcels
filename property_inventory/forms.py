from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from property_inventory.models import Property

class PropertySearchForm(forms.ModelForm):

	class Meta:
		model = Property
		fields = ['parcel', 'streetAddress', 'nsp', 'structureType', 'cdc', 'zone', 'zipcode', 'sidelot_eligible', 'homestead_only', 'bep_demolition']
	
	def __init__(self, *args, **kwargs):
		super(PropertySearchForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'PropertySearchForm'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-8'
		self.helper.form_method = 'get'
		self.helper.form_action = ''
		self.helper.add_input(Submit('submit', 'Search'))
