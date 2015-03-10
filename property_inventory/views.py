from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers

from property_inventory.models import Property

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

