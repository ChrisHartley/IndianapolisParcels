from django.shortcuts import render
from django.views.generic import View # for class based views
from django.shortcuts import render_to_response
from django.template import RequestContext

from django_tables2_reports.config import RequestConfigReport as RequestConfig


from neighborhood_associations.forms import NeighborhoodAssocationSearchForm
from neighborhood_associations.models import Neighborhood_Association
from neighborhood_associations.tables import NeighborhoodAssociationTable
from property_inventory.models import Property

# return neighborhood association contacts for given parcel
class get_relevant_neighborhood_assocations(View):

	def get(self, request):
		config = RequestConfig(request)
		parcelDoesNotExist = False
		if 'parcel' in request.GET:
			parcelNumber = request.GET.__getitem__('parcel')
			form = NeighborhoodAssocationSearchForm(request.GET)
			try:			
				selected_property = Property.objects.get(parcel=parcelNumber)
				na = Neighborhood_Association.objects.filter(geometry__contains=selected_property.geometry).order_by('area2')
			except Property.DoesNotExist:
				na = Neighborhood_Association.objects.all().order_by('name')	
				parcelDoesNotExist = True
	
		else:
			form = NeighborhoodAssocationSearchForm()
			na = Neighborhood_Association.objects.all().order_by('name')
			parcelNumber = ''

		naTable = NeighborhoodAssociationTable(na, prefix="na-")
		config.configure(naTable)

		return render_to_response('neighborhood_associations.html', {
			'form': form,
			'title': parcelNumber,
			'table': naTable,
			'parcelDoesNotExist': parcelDoesNotExist
		}, context_instance=RequestContext(request))
