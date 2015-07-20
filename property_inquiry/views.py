from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django_tables2_reports.config import RequestConfigReport as RequestConfig

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.mail import send_mail

from ipware.ip import get_real_ip

from property_inquiry.models import propertyInquiry
from property_inventory.models import Property
from property_inquiry.filters import PropertyInquiryFilters
from property_inquiry.tables import PropertyInquiryTable
from property_inquiry.forms import PropertyInquiryForm


# Displays form template for property inquiry submissions, and saves those submissions
def submitPropertyInquiry(request):
#	form = PropertyInquiryForm(request.POST or None)
	parcelNumber = False
	if request.method == 'POST':
		form = PropertyInquiryForm(request.POST)
		try:
			selected_property = Property.objects.get(parcel__exact=request.POST['parcel'])
		except Property.DoesNotExist:
			selected_property = None
		if form.is_valid():
			form_saved = form.save(commit=False)			# this is necessary so we can set the Property based on the parcel number inputed
			form_saved.Property = selected_property
			form_saved.applicant_ip_address = get_real_ip(request)
			form_saved.save()
			parcelNumber = form.cleaned_data['parcel']
			ChosenProperty = Property.objects.get(parcel__exact=parcelNumber)
			message_body = 'Applicant: ' + form.cleaned_data['applicant_name'] + '\n' + 'Parcel: ' + form.cleaned_data['parcel'] + '\nAddress: ' + ChosenProperty.streetAddress + '\nStatus: ' + ChosenProperty.status
			send_mail('New Property Inquiry', message_body, 'chris.hartley@renewindianapolis.org',
    			['chris.hartley@renewindianapolis.org'], fail_silently=False)
	form = PropertyInquiryForm()
	return render_to_response('property_inquiry.html', {
		'form': form,
		'parcel': parcelNumber,
		'title': 'property inquiry'
	}, context_instance=RequestContext(request))

# Displays submitted property inquiries
@login_required
def inquiry_list(request):
	config = RequestConfig(request)
	f = PropertyInquiryFilters(request.GET, queryset=propertyInquiry.objects.all().order_by('-timestamp'))
	table = PropertyInquiryTable(f)
	config.configure(table)
	return render_to_response('admin-with-filter-table.html', {
		'filter': f,
		'title': 'Property Inquiry Admin',
		'table': table
	}, context_instance=RequestContext(request))
