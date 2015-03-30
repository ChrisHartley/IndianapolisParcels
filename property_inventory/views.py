from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json
from django.core import serializers
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from django.views.generic import View # for class based views

from vectorformats.Formats import Django, GeoJSON    # used for geojson display of search results

from property_inventory.models import Property
from property_inventory.filters import ApplicationStatusFilters
from property_inventory.tables import PropertyStatusTable
from property_inventory.tables import PropertySearchTable
from property_inventory.forms import PropertySearchForm
from property_inventory.filters import PropertySearchFilter


def getAddressFromParcel(request):
	response_data = {}
	if 'parcel' in request.GET and request.GET['parcel']:
		parcelNumber = request.GET.__getitem__('parcel')
		try:
			SearchResult = Property.objects.get(parcel__exact=parcelNumber)
		except Property.DoesNotExist:
			return HttpResponse("No such parcel in our inventory", content_type="text/plain")
		response_data['streetAddress'] = SearchResult.streetAddress
		response_data['structureType'] = SearchResult.structureType
		response_data['status'] = SearchResult.status
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	if 'streetAddress' in request.GET and request.GET['streetAddress']:
		streetAddress = request.GET.__getitem__('streetAddress')
		try:
			SearchResult = Property.objects.get(streetAddress__iexact=streetAddress)
		except Property.DoesNotExist:
			return HttpResponse("No such address in our inventory", content_type="text/plain") 
		return HttpResponse(SearchResult.parcel)
	return HttpResponse("Please submit a search term")

# Given a street name, return a json object with all the properties in inventory 
def getMatchingAddresses(request):
#	response_data = {}
	if 'street_name' in request.GET and request.GET['street_name']:
		street_name = request.GET.__getitem__('street_name')
		try:
			SearchResult = Property.objects.filter(streetAddress__icontains=street_name)
		except Property.DoesNotExist:
			return HttpResponse("No such properties in our inventory", content_type="text/plain")

		response_data = serializers.serialize('json', SearchResult, fields=('parcel','streetAddress'))
		return HttpResponse(response_data, content_type="application/json")
	return HttpResponse("Please submit a search term")

# Show a table with property statuses by sold and approved (in-progress). 
def	showApplications(request):
	config = RequestConfig(request)

	soldProperties = Property.objects.all().filter(status__exact='Sold').order_by('status', 'applicant')
	approvedProperties = Property.objects.all().filter(status__istartswith='Sale').order_by('status', 'applicant')

	soldFilter = ApplicationStatusFilters(request.GET, queryset=soldProperties, prefix="sold-") 
	approvedFilter = ApplicationStatusFilters(request.GET, queryset=approvedProperties, prefix="approved-") 

	soldTable = PropertyStatusTable(soldFilter, prefix="sold-")
	approvedTable = PropertyStatusTable(approvedFilter, prefix="approved-")

	config.configure(soldTable)
	config.configure(approvedTable)
	return render(request, 'app_status_template.html', {'soldTable': soldTable, 'approvedTable': approvedTable, 'title': 'applications & sale activity', 'soldFilter': soldFilter, 'approvedFilter': approvedFilter})

# search property inventory
def searchProperties(request):
	config = RequestConfig(request)

	f = PropertySearchFilter(request.GET, queryset=Property.objects.filter(propertyType__exact='lb'), prefix="property") 
	table = PropertySearchTable(f, prefix="property")
	config.configure(table)

	if 'returnType' in request.GET and request.GET['returnType']:
		if request.GET['returnType'] == "geojson":
			djf = Django.Django(geodjango='geometry', properties=['streetAddress', 'parcel', 'status', 'structureType', 'sidelot_eligible', 'homestead_only', 'price'])
			geoj = GeoJSON.GeoJSON()
			s = geoj.encode(djf.decode(f))
			return HttpResponse(s)

	return render_to_response('property_search.html', {
		'form': f.form,
		'title': 'Property Search',
		'table': table
	}, context_instance=RequestContext(request))
