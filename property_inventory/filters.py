import django_filters
from django_filters import MethodFilter
from django.db.models import Count, Q
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.gis.geos import GEOSGeometry  # used for centroid calculation

from property_inventory.models import Property, Zoning
from property_inventory.forms import PropertySearchForm

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


class ChoiceMethodFilter(django_filters.MethodFilter):
    field_class = forms.ChoiceField


class PropertySearchFilter(django_filters.FilterSet):
    streetAddress = django_filters.CharFilter(
        lookup_type='icontains', label="Street address")
    parcel = django_filters.CharFilter(
        lookup_type='icontains', label="Parcel number")
    st = Property.objects.order_by('structureType').distinct(
        'structureType').values_list('structureType', flat=True).order_by('structureType')
    structure_types = zip(st, st)
    structureType = django_filters.MultipleChoiceFilter(
        choices=structure_types, name='structureType', label='Structure Type')

    status_choices = [('available', 'Available'), ('review', 'Application under review'),
                      ('approved', 'Approved for Sale'), ('sold', 'Sold')]
    #status = django_filters.MultipleChoiceFilter(choices=status_choices, required=False, lookup_type='icontains')
    status = ChoiceMethodFilter(
        label='Status', widget=forms.Select, action='filter_status', choices=status_choices)

    # structureType = django_filters.ModelMultipleChoiceFilter(
    # 	queryset=Property.objects.order_by('structureType').distinct('structureType').values('structureType'),
    # 	to_field_name="structureType",
    # 	label="Structure Type",
    # )

    #structureType = django_filters.ModelMultipleChoiceFilter(queryset=Property.objects.values_list('structureType', flat=True).distinct('structureType').order_by('structureType'), to_field_name="structureType", label="Structure Type")
    #zoning = django_filters.ModelMultipleChoiceFilter(queryset=Zoning.objects.values_list('name', flat=True).distinct('name').order_by('name'), to_field_name="name", label="Zoning")

    #zoning = forms.ModelMultipleChoiceField(queryset=Zoning.objects.all().order_by('name'), required=False)
    #zipcode = forms.ModelMultipleChoiceField(queryset=Zipcode.objects.all().order_by('name'), required=False)
    #cdc = forms.ModelMultipleChoiceField(queryset=CDC.objects.all().order_by('name'), required=False)

    searchArea = MethodFilter(action="filter_searchArea")

    class Meta:
        model = Property
        #fields = ['parcel', 'streetAddress', 'nsp', 'structureType', 'cdc', 'zone', 'sidelot_eligible', 'homestead_only', 'bep_demolition']
        form = PropertySearchForm

    def filter_status(self, queryset, value):
        if value == 'available':
            return queryset.filter(status__icontains='Available')
        if value == 'review':
            return queryset.filter(
                (Q(renew_owned__exact=False) & Q(
                    status__icontains='Sale approved by Board of Directors'))
                | Q(status__icontains='Sale approved by Review Committee')
            )
        if value == 'approved':
            return queryset.filter(
                (Q(renew_owned__exact=True) & Q(
                    status__icontains='Sale approved by Board of Directors'))
                | Q(status__icontains='Sale approved by MDC')
            )
        if value == 'sold':
            return queryset.filter(status__contains='Sold')

        return queryset

    def filter_searchArea(self, queryset, value):
        try:
            searchGeometry = GEOSGeometry(value, srid=900913)
        except Exception:
            return queryset

        return queryset.filter(
            geometry__within=searchGeometry
        )
