import django_filters

from .models import annual_report

# this allows a None option with the AllValues dropdown.
class AllValuesNoneFilter(django_filters.ChoiceFilter):
	@property
	def field(self):
		qs = self.model._default_manager.distinct()
		qs = qs.order_by(self.name).values_list(self.name, flat=True)
		self.extra['choices'] = [(o, o) for o in qs]
		self.extra['choices'].insert(0, ('', u'------',))
		return super(AllValuesNoneFilter, self).field


class AnnualReportFilters(django_filters.FilterSet):
	Property__streetAddress = django_filters.CharFilter(lookup_type='icontains', label='Street Address')
	name = django_filters.CharFilter(lookup_type='icontains')
	organization = django_filters.CharFilter(lookup_type='icontains')
	email = django_filters.CharFilter(lookup_type='icontains')
	all_buyers = AllValuesNoneFilter(name='name', label="Buyer")
	
	class Meta:
		model = annual_report
		fields = ['Property__streetAddress', 'parcel', 'name', 'email', 'all_buyers']

