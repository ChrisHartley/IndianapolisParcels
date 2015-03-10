from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from annual_report_form.models import annual_report
from annual_report_form.forms import annualReportForm
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
