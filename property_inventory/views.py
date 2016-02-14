from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json  # not used anymore, right?
from django.core import serializers
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from django.views.generic import View  # for class based views

# used for geojson display of search results
from vectorformats.Formats import Django, GeoJSON
from django.core.serializers import serialize  # new in 1.8 supports geojson
from django.http import JsonResponse
from django.core.serializers.json import Serializer
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer
from django.utils.encoding import is_protected_type

# these used for search() function, can be removed when that is removed
# used for geojson display of search results
from vectorformats.Formats import Django, GeoJSON
import csv  # used for csv return of search results
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import operator
from django.contrib.gis.geos import GEOSGeometry  # used for centroid calculation
from djqscsv import render_to_csv_response

from property_inventory.models import Property, Zipcode, CDC, Zoning
from property_inventory.filters import ApplicationStatusFilters
from property_inventory.tables import PropertyStatusTable
from property_inventory.tables import PropertySearchTable
from property_inventory.forms import PropertySearchForm, SearchForm
from property_inventory.filters import PropertySearchFilter

def get_inventory_csv(request):
    qs = Property.objects.all().values('parcel', 'streetAddress', 'zipcode__name', 'zone__name','cdc__name', 'applicant', 'status','area', 'price', 'price_obo')
    #qs = Property.objects.all().prefetch_related('cdc', 'zone', 'zipcode')
    return render_to_csv_response(qs)

def show_all_properties(request):
    #all_prop_select = Property.objects.all().select_related('cdc', 'zone', 'zipcode')
    all_prop_select = None
    all_prop_prefetch = Property.objects.all().prefetch_related('cdc', 'zone', 'zipcode')

    return render(request, 'testing.html', {'all_properties_select': all_prop_select, 'all_properties_prefetch': all_prop_prefetch})

# given a parcel number return a json with a number of fields


def getAddressFromParcel(request):
    if 'parcel' in request.GET and request.GET['parcel']:
        parcelNumber = request.GET.__getitem__('parcel')
        SearchResult = Property.objects.filter(parcel__exact=parcelNumber)
        response_data = serializers.serialize('json', SearchResult,
                                              fields=('streetAddress', 'zipcode', 'status', 'structureType',
                                                      'sidelot_eligible', 'homestead_only', 'price', 'nsp')
                                              )
        return HttpResponse(response_data, content_type="application/json")
    # when is this used? who knows. I broke it, when I find out where it is used I'll fix it.
    # if 'streetAddress' in request.GET and request.GET['streetAddress']:
    # 	streetAddress = request.GET.__getitem__('streetAddress')
    # 	try:
    # 		SearchResult = Property.objects.get(streetAddress__iexact=streetAddress)
    # 		return HttpResponse(SearchResult.parcel)
    # 	except Property.DoesNotExist:
    return HttpResponse("Please submit a search term")

# Show a table with property statuses by sold and approved (in-progress).


def showApplications(request):
    config = RequestConfig(request)

    soldProperties = Property.objects.all().filter(
        status__istartswith='Sold').order_by('status', 'applicant')
    approvedProperties = Property.objects.all().filter(
        status__istartswith='Sale').order_by('status', 'applicant')

    soldFilter = ApplicationStatusFilters(
        request.GET, queryset=soldProperties, prefix="sold-")
    approvedFilter = ApplicationStatusFilters(
        request.GET, queryset=approvedProperties, prefix="approved-")

    soldTable = PropertyStatusTable(soldFilter, prefix="sold-")
    approvedTable = PropertyStatusTable(approvedFilter, prefix="approved-")

    config.configure(soldTable)
    config.configure(approvedTable)
    return render(request, 'app_status_template.html', {'soldTable': soldTable, 'approvedTable': approvedTable, 'title': 'applications & sale activity', 'soldFilter': soldFilter, 'approvedFilter': approvedFilter})


class DisplayNameJsonSerializer(GeoJSONSerializer):

    def handle_field(self, obj, field):
        value = field._get_val_from_obj(obj)

        display_method = "get_%s_display" % field.name
        if hasattr(obj, display_method):
            self._current[field.name] = getattr(obj, display_method)()
        elif is_protected_type(value):
            self._current[field.name] = value
        else:
            if field == "price":
                self._current[field.name] = "$".join(
                    field.value_to_string(obj))
            else:
                self._current[field.name] = field.value_to_string(obj)


# search property inventory - new version
def searchProperties(request):
    #	config = RequestConfig(request)
    f = PropertySearchFilter(request.GET, queryset=Property.objects.filter(
        propertyType__exact='lb', is_active__exact=True).prefetch_related('cdc', 'zone', 'zipcode'))

    if 'returnType' in request.GET and request.GET['returnType']:
        if request.GET['returnType'] == "geojson":
            json_serializer = DisplayNameJsonSerializer()
            s = serializers.serialize('geojson',
                                      f,
                                      geometry_field='geometry',
                                      fields=('id', 'parcel', 'streetAddress', 'zipcode', 'zone', 'status', 'structureType',
                                              'sidelot_eligible', 'homestead_only', 'price', 'nsp', 'renew_owned', 'price_obo', 'cdc', 'geometry'),
                                      use_natural_foreign_keys=True
                                      )
            return HttpResponse(s, content_type='application/json')

    return render(
        request,
        'property_search.html',
        {
            'form_filter': f.form,
            'title': 'Property Search'
        })


# used by dataTables -- not used anymore?
# def propertiesAsJSON(request):
# 	object_list = Property.objects.filter(is_active__exact=True)
# 	json = serializers.serialize('json', object_list, use_natural_foreign_keys=True)
# 	return HttpResponse(json, content_type='application/json')

# populate property popup on map via ajax
def propertyPopup(request):
    object_list = Property.objects.get(parcel__exact=request.GET['parcel'])
#	json = serializers.serialize('json', object_list)
    content = "<div style='font-size:.8em'>Parcel: " + str(object_list.parcel) + "<br>Address: " + str(object_list.streetAddress) + "<br>Status: " + str(object_list.status) + "<br>Structure Type: " + str(
        object_list.structureType) + "<br>Side lot Eligible: " + str(object_list.sidelot_eligible) + "<br>Homestead only: " + str(object_list.homestead_only) + "</div>"
    return HttpResponse(content, content_type='text/plain; charset=utf8')
#	return HttpResponse(json, content_type='application/json')
