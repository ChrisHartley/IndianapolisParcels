import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from property_inventory.models import Property

# this allows a None option with the AllValues dropdown.
class AllValuesNoneFilter(django_filters.ChoiceFilter):
	@property
	def field(self):
		qs = self.model._default_manager.distinct()
		qs = qs.order_by(self.name).values_list(self.name, flat=True)
		self.extra['choices'] = [(o, o) for o in qs]
		self.extra['choices'].insert(0, ('', u'------',))
		return super(AllValuesNoneFilter, self).field

class ApplicationStatusFilters(django_filters.FilterSet):
	streetAddress = django_filters.CharFilter(lookup_type='icontains')
	all_applicants = AllValuesNoneFilter(name='applicant', label="Applicant")

	def __init__(self, *args, **kwargs):
		super(ApplicationStatusFilters, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-inline'
		self.helper.form_method = 'get'
		self.helper.add_input(Submit('Filter', 'Filter'))

	class Meta:
		model = Property
		fields = ['all_applicants', 'streetAddress']
