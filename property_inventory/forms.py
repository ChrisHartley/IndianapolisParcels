from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, Button, HTML, Div
from crispy_forms.bootstrap import FormActions
from django.forms.widgets import HiddenInput, SelectMultiple
from property_inventory.models import Property, Zipcode, CDC, Zoning

# new search form
class PropertySearchForm(forms.ModelForm):
	#zoning = forms.ModelMultipleChoiceField(queryset=Zoning.objects.all().order_by('name'), required=False)
	#zipcodes = forms.ModelMultipleChoiceField(queryset=Zipcode.objects.all().order_by('name'), required=False)
	#zipcode1 = forms.ModelChoiceField(queryset=Zipcode.objects.all().order_by('name'), required=False)
	#cdc = forms.ModelMultipleChoiceField(queryset=CDC.objects.all().order_by('name'), required=False)
	searchArea = forms.CharField(required=False, widget=HiddenInput())
	status_choices = [('Available','Available'), ('Sale','Application under review'), ('MDC','Approved for Sale'), ('Sold','Sold')]
	status = forms.MultipleChoiceField(choices=status_choices, required=False)



	class Meta:
		model = Property
		fields = ['parcel', 'streetAddress', 'nsp', 'zipcode', 'zone', 'sidelot_eligible', 'homestead_only', 'bep_demolition', 'renew_owned', 'price_obo', 'searchArea']

	def __init__(self, *args, **kwargs):
		super(PropertySearchForm, self).__init__(*args, **kwargs)
		self.fields['searchArea'].widget = HiddenInput()
		self.helper = FormHelper()
		self.helper.form_id = 'PropertySearchForm'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-8'
		self.helper.render_unmentioned_fields = False

		self.helper.form_method = 'get'
		self.helper.form_action = ''
		self.helper.layout = Layout(
			Fieldset(
				'Search',
				HTML('<input type="checkbox" onclick="toggleDraw(this);" name="searchPolygon" value="polygon">Draw search area on map</input>'),
				Field('parcel'),
				Field('streetAddress'),
				Field('status'),
			),
			Fieldset('',HTML('<button id="searchToggle">Show more search options >>></button><br/>')),
			Fieldset(
				'',
				Field('nsp'),
				Field('structureType'),
				Field('cdc'),
				Field('zone'),
				Field('zipcode'),
				Field('sidelot_eligible'),
				Field('homestead_only'),
				Field('bep_demolition'),
				Field('renew_owned'),
				Field('price_obo'),
			 css_class='moreSearchOptions'),
			FormActions(
				Button('cancel', 'Reset'),
				Submit('save', 'Search')
			)
		)

# old property search form - remove in v2.0
class SearchForm(forms.ModelForm):
	zipcode = forms.ModelMultipleChoiceField(queryset=Zipcode.objects.all().order_by('name'), widget=forms.SelectMultiple, help_text="The 5 digit zipcode.", label='Zipcode')
	cdc = forms.ModelMultipleChoiceField(queryset=CDC.objects.all().order_by('name'), widget=forms.SelectMultiple, help_text="The Community Development Corporation boundaries the property falls within.", label='CDC')
	zone = forms.ModelMultipleChoiceField(queryset=Zoning.objects.filter(id__in=Property.objects.distinct('zone').values('zone').filter(propertyType__exact='lb')).order_by('name'), widget=forms.SelectMultiple, help_text="The zoning of the property.", label='Zoning')
	structureType = forms.ModelMultipleChoiceField(queryset=Property.objects.distinct('structureType').order_by('structureType').filter(propertyType__exact='lb').values_list('structureType', flat=True), widget=forms.SelectMultiple, help_text='As classified by the Assessor.', label='Structure Type')
	minsize = forms.IntegerField(label="Minimum parcel size", help_text='Area is in square feet.')
	maxsize = forms.IntegerField(label="Maximum parcel size", help_text='Area is in square feet.')
	nsp = forms.ChoiceField(widget=forms.Select, label='NSP', help_text="If a property comes with requirements related to the Neighborhood Stabilization Program.", choices = (('1', 'Yes'), ('0', 'No'), ('', '') ), initial='')
	sidelot_eligible = forms.ChoiceField(widget=forms.Select, label='Side lot', help_text="If a property is eligible for the side lot program.", choices = (('1', 'Yes'), ('0', 'No'), ('', '') ), initial='')
	homestead_only = forms.ChoiceField(widget=forms.Select, label='Homestead Only', help_text="If a property is available only for homestead applications.", choices = (('1', 'Yes'), ('0', 'No'), ('', '') ), initial='')
	bep_demolition = forms.ChoiceField(widget=forms.Select, label='Slated for BEP Demolition', help_text="If a property is currently on the list for demolition using BEP funds. Demolition can be stopped if a viable plan for reuse is presented.", choices = (('1', 'Yes'), ('0', 'No'), ('', '') ), initial='')
	status = forms.ModelMultipleChoiceField(queryset=Property.objects.distinct('status').values_list('status', flat=True), widget=forms.Select, label='Property Status', help_text="If a property is sold, pending or available")

	class Meta:
		model = Property
		fields = ['parcel', 'streetAddress', 'nsp', 'structureType', 'cdc', 'zone', 'zipcode', 'sidelot_eligible', 'homestead_only', 'bep_demolition', 'status']
