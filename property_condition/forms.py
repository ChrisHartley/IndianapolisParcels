from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Button, MultiField, Field
from crispy_forms.bootstrap import FormActions
from property_condition.models import ConditionReport
from property_inventory.models import Property

class ConditionReportForm(forms.ModelForm):
	Property = forms.ModelChoiceField(queryset=Property.objects.exclude(structureType__exact='Vacant Lot').order_by('streetAddress'))	

	class Meta:
		model = ConditionReport
		exclude = []
			
	def __init__(self, *args, **kwargs):
		super(ConditionReportForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'ConditionReportForm'
		self.helper.form_class = 'form-horizontal'
		#self.helper.field_template = 'bootstrap3/layout/inline_field_custom.html'
#		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-8'
		self.helper.label_class = 'col-lg-2'
		self.helper.layout = Layout(
			Fieldset(
				'Property Condition Report',
				'Property'
			),
			Fieldset(
				'Roof',
				Div('roof_shingles', 'roof_shingles_notes'),
				Div('roof_framing',	'roof_framing_notes'),
				Div('roof_gutters', 'roof_gutters_notes'),
			),
			Fieldset(
				'Foundation',
				Div('foundation_slab', 'foundation_slab_notes'),
				Div('foundation_crawl', 'foundation_crawl_notes'),
			),
			Fieldset(
				'Exterior Siding',
				Div('exterior_siding_brick', 'exterior_siding_brick_notes'),
				Div('exterior_siding_vinyl', 'exterior_siding_vinyl_notes'),
				Div('exterior_siding_wood', 'exterior_siding_wood_notes'),
				Div('exterior_siding_other', 'exterior_siding_other_notes'),
			),
			Fieldset(
				'Miscellaneous',
				Div('windows', 'windows_notes'),
				Div('garage', 'garage_notes'),
				Div('fencing', 'fencing_notes'),
				Div('landscaping', 'landscaping_notes'),
				Div('doors', 'doors_notes'),
				Div('kitchen_cabinets', 'kitchen_cabinets_notes'),
			),
			Fieldset(
				'Flooring',
				Div('flooring_subflooring', 'flooring_subflooring_notes'),
				Div('flooring_covering', 'flooring_covering_notes'),
			),
			Fieldset(
				'Electrical',
				Div('electrical_knob_tube_cloth', 'electrical_knob_tube_cloth_notes'),
				Div('electrical_standard', 'electrical_standard_notes'),
			),
			Fieldset(
				'Plumbing',
				Div('plumbing_metal', 'plumbing_metal_notes'),
				Div('plumbing_plastic', 'plumbing_plastic_notes'),
			),
			Fieldset(
				'Walls',
				Div('walls_drywall', 'walls_drywall_notes'),
				Div('walls_lathe_plaster', 'walls_lathe_plaster_notes'),
			),
			Fieldset(
				'HVAC',
				Div('hvac_furance', 'hvac_furance_notes'),
				Div('hvac_duct_work', 'hvac_duct_work_notes'),
				Div('hvac_air_conditioner', 'hvac_air_conditioner_notes'),
			),
 			FormActions(
				Button('cancel', 'Cancel'),
				Submit('save', 'Save changes')
			)
		)
		self.helper.form_method = 'post'
		self.helper.form_action = ''


