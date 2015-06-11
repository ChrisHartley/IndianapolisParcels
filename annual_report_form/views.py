from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django_tables2_reports.config import RequestConfigReport as RequestConfig

from annual_report_form.models import annual_report
from annual_report_form.forms import annualReportForm
from annual_report_form.filters import AnnualReportFilters
from annual_report_form.tables import AnnualReportTable
from property_inventory.models import Property

# Displays form template for annual reports from property owners, and saves those submissions
def showAnnualReportForm(request):
	form = annualReportForm(request.POST or None)
	success = False
	if request.method == 'POST':
		form = annualReportForm(request.POST, request.FILES)
		try:
			selected_property = Property.objects.get(parcel__exact=request.POST['parcel'])
		except Property.DoesNotExist:
			selected_property = None
		if form.is_valid():
			form_saved = form.save(commit=False)			# this is necessary so we can set the Property based on the parcel number inputed
			form_saved.Property = selected_property
			form_saved.save()
			success = True
		else:
			print form.errors
	return render_to_response('annual_report_form.html', {
		'form': form,
		'success': success,
		'title': "annual report"
	}, context_instance=RequestContext(request))

def showAnnualReportData(request, id):
	selected_report = get_object_or_404(annual_report, id=id)
	title = selected_report.Property.streetAddress + " - annual report"

	try:
	    next = annual_report.objects.filter(pk__gt=selected_report.pk).order_by('id').first()
	except annual_report.DoesNotExist:
	    next = None
	try:
	    pre = annual_report.objects.filter(pk__lt=selected_report.pk).order_by('id').last()
	except annual_report.DoesNotExist:
	    pre = None

	title = selected_report.Property.streetAddress + " - annual report"

	return render_to_response('annual_report_viewer.html', {
		'record': selected_report,
		'title': title,
		'next': next,
		'pre': pre,
	}, context_instance=RequestContext(request))

def showAnnualReportIndex(request):
	config = RequestConfig(request)
	f = AnnualReportFilters(request.GET, queryset=annual_report.objects.all().order_by('id')) 
	table = AnnualReportTable(f)
	config.configure(table)
	return render_to_response('admin-with-filter-table.html', {
		'filter': f, 
		'title': 'Annual Report Admin',
		'table': table
	}, context_instance=RequestContext(request))


