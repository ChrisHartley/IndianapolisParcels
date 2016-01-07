import django_filters

from property_inquiry.models import propertyInquiry

# this allows a None option with the AllValues dropdown.
class AllValuesNoneFilter(django_filters.ChoiceFilter):
	@property
	def field(self):
		qs = self.model._default_manager.distinct()
		qs = qs.order_by(self.name).values_list(self.name, flat=True)
		self.extra['choices'] = [(o, o) for o in qs]
		self.extra['choices'].insert(0, ('', u'------',))
		return super(AllValuesNoneFilter, self).field


class PropertyInquiryFilters(django_filters.FilterSet):
	timestamp = django_filters.DateRangeFilter()
	#applicant_name = django_filters.CharFilter(lookup_type='icontains')
	#applicant_email_address = django_filters.CharFilter(lookup_type='icontains')
	#all_applicants = AllValuesNoneFilter(name='user', label="Applicant")
	Property__streetAddress = django_filters.CharFilter(lookup_type='icontains', label='Street Address')
	user__email = AllValuesNoneFilter(label="Email")
	#name =

	class Meta:
		model = propertyInquiry
		fields = ('Property', 'timestamp', 'user__email')
