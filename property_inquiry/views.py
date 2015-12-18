from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django_tables2_reports.config import RequestConfigReport as RequestConfig

from django.shortcuts import render_to_response, HttpResponseRedirect
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
		if form.is_valid():
			form_saved = form.save(commit=False)
			form_saved.applicant_ip_address = get_real_ip(request)
			form_saved.user = request.user
			form_saved.save()
			message_body = 'Applicant: ' + form_saved.user.first_name + ' ' + form_saved.user.last_name + '\n' + 'Parcel: ' + form_saved.Property.parcel + '\nAddress: ' + form_saved.Property.streetAddress + '\nStatus: ' + form_saved.Property.status
			send_mail('New Property Inquiry', message_body, 'chris.hartley@renewindianapolis.org',
    			['chris.hartley@renewindianapolis.org'], fail_silently=False)
			return HttpResponseRedirect('/inquiry-thank-you')
	form = PropertyInquiryForm()
	return render_to_response('property_inquiry.html', {
		'form': form,
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
