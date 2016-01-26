import django_filters

from .models import ConditionReport

# this allows a None option with the AllValues dropdown.


class AllValuesNoneFilter(django_filters.ChoiceFilter):

    @property
    def field(self):
        qs = self.model._default_manager.distinct()
        qs = qs.order_by(self.name).values_list(self.name, flat=True)
        self.extra['choices'] = [(o, o) for o in qs]
        self.extra['choices'].insert(0, ('', u'------',))
        return super(AllValuesNoneFilter, self).field


class ConditionReportFilters(django_filters.FilterSet):
    Property__streetAddress = django_filters.CharFilter(
        lookup_type='icontains', label='Street Address')

    class Meta:
        model = ConditionReport
        fields = ['Property__parcel', 'Property__streetAddress']
