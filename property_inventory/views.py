from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json # not used anymore, right?
from django.core import serializers
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from django.views.generic import View # for class based views

from vectorformats.Formats import Django, GeoJSON    # used for geojson display of search results
from django.core.serializers import serialize # new in 1.8 supports geojson
from django.http import JsonResponse
from django.core.serializers.json import Serializer
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer
from django.utils.encoding import is_protected_type

# these used for search() function, can be removed when that is removed
from vectorformats.Formats import Django, GeoJSON    # used for geojson display of search results
import csv # used for csv return of search results
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import operator
from django.contrib.gis.geos import GEOSGeometry # used for centroid calculation

from property_inventory.models import Property, Zipcode, CDC, Zoning
from property_inventory.filters import ApplicationStatusFilters
from property_inventory.tables import PropertyStatusTable
from property_inventory.tables import PropertySearchTable
from property_inventory.forms import PropertySearchForm, SearchForm
from property_inventory.filters import PropertySearchFilter

# given a parcel number return a json with a number of fields
def getAddressFromParcel(request):
	if 'parcel' in request.GET and request.GET['parcel']:
		parcelNumber = request.GET.__getitem__('parcel')
		SearchResult = Property.objects.filter(parcel__exact=parcelNumber)
		response_data = serializers.serialize('json', SearchResult,
			fields=('streetAddress', 'zipcode','status', 'structureType', 'sidelot_eligible', 'homestead_only', 'price', 'nsp')
			)
		return HttpResponse(response_data, content_type="application/json")
	## when is this used? who knows. I broke it, when I find out where it is used I'll fix it.
	# if 'streetAddress' in request.GET and request.GET['streetAddress']:
	# 	streetAddress = request.GET.__getitem__('streetAddress')
	# 	try:
	# 		SearchResult = Property.objects.get(streetAddress__iexact=streetAddress)
	# 		return HttpResponse(SearchResult.parcel)
	# 	except Property.DoesNotExist:
	return HttpResponse("Please submit a search term")

# Given a street name, return a json object with all the properties in inventory
def getMatchingAddresses(request):
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

	soldProperties = Property.objects.all().filter(status__istartswith='Sold').order_by('status', 'applicant')
	approvedProperties = Property.objects.all().filter(status__istartswith='Sale').order_by('status', 'applicant')

	soldFilter = ApplicationStatusFilters(request.GET, queryset=soldProperties, prefix="sold-")
	approvedFilter = ApplicationStatusFilters(request.GET, queryset=approvedProperties, prefix="approved-")

	soldTable = PropertyStatusTable(soldFilter, prefix="sold-")
	approvedTable = PropertyStatusTable(approvedFilter, prefix="approved-")

	config.configure(soldTable)
	config.configure(approvedTable)
	return render(request, 'app_status_template.html', {'soldTable': soldTable, 'approvedTable': approvedTable, 'title': 'applications & sale activity', 'soldFilter': soldFilter, 'approvedFilter': approvedFilter})

# old search function from renew-django - will be removed in v2.0
@csrf_exempt
def search(request):
	queries = []
	properties = Property.objects.all()
	if request.GET.items():
		if 'searchType' in request.GET and request.GET['searchType']:
			searchType = request.GET.__getitem__('searchType')
			if searchType == "lb":
				queries.append(Q(propertyType__exact=searchType))
			if searchType == "sp":
				queries.append(Q(propertyType__exact=searchType))
		if 'parcel' in request.GET and request.GET['parcel']:
			parcelNumber = request.GET.__getitem__('parcel')
			queries.append(Q(parcel__exact=parcelNumber))
		if 'streetAddress' in request.GET and request.GET['streetAddress']:
			streetAddress = request.GET.__getitem__('streetAddress')
			queries.append(Q(streetAddress__icontains=streetAddress))
		if 'minsize' in request.GET and request.GET['minsize']:
			minsize = request.GET.__getitem__('minsize')
			queries.append(Q(area__gte=minsize))
		if 'maxsize' in request.GET and request.GET['maxsize']:
			minsize = request.GET.__getitem__('maxsize')
			queries.append(Q(area__lte=minsize))
		if 'zipcode' in request.GET and request.GET['zipcode']:
			zipcode = request.GET.getlist('zipcode')
			queries.append(Q(zipcode__in=Zipcode.objects.filter(id__in=zipcode)))
		if 'cdc' in request.GET and request.GET['cdc']:
			cdc = request.GET.getlist('cdc')
			queries.append(Q(cdc__in=CDC.objects.filter(id__in=cdc)))
		if 'zone' in request.GET and request.GET['zone']:
			zone = request.GET.getlist('zone')
			queries.append(Q(zone__in=Zoning.objects.filter(id__in=zone)))
		if 'structureType' in request.GET and request.GET['structureType']:
			structureType = request.GET.getlist('structureType')
			queries.append(Q(structureType__in=structureType))
		if 'nsp' in request.GET and request.GET['nsp']:
			nsp = request.GET.__getitem__('nsp')
			queries.append(Q(nsp=nsp))
		if 'sidelot_eligible' in request.GET and request.GET['sidelot_eligible']:
			sidelot_eligible = request.GET.__getitem__('sidelot_eligible')
			queries.append(Q(sidelot_eligible=sidelot_eligible))
		if 'homestead_only' in request.GET and request.GET['homestead_only']:
			homestead_only = request.GET.__getitem__('homestead_only')
			queries.append(Q(homestead_only=homestead_only))
		if 'bep_demolition' in request.GET and request.GET['bep_demolition']:
			bep_demolition = request.GET.__getitem__('bep_demolition')
			queries.append(Q(bep_demolition=bep_demolition))
		if 'searchArea' in request.GET and request.GET['searchArea']:
			searchArea = request.GET.__getitem__('searchArea')
			try:
				searchGeometry = GEOSGeometry(searchArea, srid=900913)
			except Exception:
				pass
			else:
				queries.append(Q(geometry__within=searchGeometry))
		if 'returnType' in request.GET and request.GET['returnType']:
			returnType = request.GET.__getitem__('returnType')
			try:
				properties = Property.objects.filter(reduce(operator.and_, queries))
			except:
				pass # search engines keep sending malformed queries with no search criteria so we want to just return everything in that case
			if returnType == "html":
				return render(request, 'property_search_table_template.html', {'table': properties})
			if returnType == "csv":
				response = HttpResponse(content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename="renew-properties.csv"'
				writer = csv.writer(response)
				writer.writerow(["Parcel Number", "Street Address", "Zipcode", "Structure Type", "CDC", "Zoned", "NSP", "Licensed Urban Garden", "Quiet Title", "Sidelot Eligible", "Homestead Only", "BEP Demolition Slated", "Parcel Area ft^2", "Status", "Price", "Price is Or Best Offer", "Lat/Lon"])
				for row in properties:
					if row.nsp:
						nspValue = "Yes"
					else:
						nspValue = "No"
					if row.urban_garden:
						ugValue = "Yes"
					else:
						ugValue = "No"
					if row.quiet_title_complete:
						qtValue = "Yes"
					else:
						qtValue = "No"
					if row.sidelot_eligible:
						slValue = "Yes"
					else:
						slValue = "No"
					if row.homestead_only:
						hstdValue = "Yes"
					else:
						hstdValue = "No"
					if row.bep_demolition:
						bepDemolition = "Yes"
					else:
						bepDemolition = "No"
					if row.price_obo:
						priceOBO = "Yes"
					else:
						priceOBO = "No"

					writer.writerow([row.parcel, row.streetAddress, row.zipcode, row.structureType, row.cdc, row.zone, nspValue, ugValue, qtValue, slValue, hstdValue, bepDemolition, row.area, row.status, row.price, priceOBO, GEOSGeometry(row.geometry).centroid])
				return response

	try:
		properties = Property.objects.filter(reduce(operator.and_, queries))
	except:
		pass
	djf = Django.Django(geodjango='geometry', properties=['streetAddress', 'parcel', 'status', 'structureType', 'sidelot_eligible', 'homestead_only', 'price'])
	geoj = GeoJSON.GeoJSON()
	s = geoj.encode(djf.decode(properties))
	return HttpResponse(s)



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
				self._current[field.name] = "$".join(field.value_to_string(obj))
			else:
				self._current[field.name] = field.value_to_string(obj)



# search property inventory - new version
def searchProperties(request):
#	config = RequestConfig(request)
	form = SearchForm()
	f = PropertySearchFilter(request.GET, queryset=Property.objects.filter(propertyType__exact='lb', is_active__exact=True), prefix="property")

	if 'returnType' in request.GET and request.GET['returnType']:
		if request.GET['returnType'] == "geojson":
			json_serializer = DisplayNameJsonSerializer()
			s = serializers.serialize('geojson',
				f,
			 	geometry_field='geometry',
			 	fields=('id', 'parcel', 'streetAddress', 'zipcode', 'status', 'structureType', 'sidelot_eligible', 'homestead_only', 'price', 'nsp', 'renew_owned', 'price_obo', 'geometry'),
			 	use_natural_foreign_keys=True
			 	)
			return HttpResponse(s, content_type='application/json')

	return render_to_response('property_search.html', {
		'form_filter': f.form,
		'form': form,
		'title': 'Property Search'
#		'table': table
	}, context_instance=RequestContext(request))

# used by dataTables
def propertiesAsJSON(request):
	object_list = Property.objects.filter(is_active__exact=True)
	json = serializers.serialize('json', object_list, use_natural_foreign_keys=True)
	return HttpResponse(json, content_type='application/json')

# populate property popup on map via ajax
def propertyPopup(request):
	object_list = Property.objects.get(parcel__exact=request.GET['parcel'])
#	json = serializers.serialize('json', object_list)
	content = "<div style='font-size:.8em'>Parcel: " + str(object_list.parcel) +"<br>Address: " + str(object_list.streetAddress)+"<br>Status: " +str(object_list.status) + "<br>Structure Type: "+ str(object_list.structureType) + "<br>Side lot Eligible: "+ str(object_list.sidelot_eligible) + "<br>Homestead only: " + str(object_list.homestead_only) + "</div>"
	return HttpResponse(content, content_type='text/plain; charset=utf8')
#	return HttpResponse(json, content_type='application/json')

# for old style search page - remove in v2.0
def showMap(request):
	form = SearchForm()
	return render_to_response('show_map.html', {
		'form': form,
		'title': 'Property Search'
	}, context_instance=RequestContext(request))
