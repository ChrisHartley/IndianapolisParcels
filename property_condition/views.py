from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from property_inventory.models import Property
from property_condition.forms import ConditionReportForm


# Displays form template for property inquiry submissions, and saves those submissions
def submitConditionReport(request):
	parcelNumber = False
	success = False
	if request.method == 'POST':
		form = ConditionReportForm(request.POST)
		if form.is_valid():
			form.save()
			success = True
	form = ConditionReportForm()
	return render_to_response('condition_report.html', {
		'form': form,
		'title': 'condition report',
		'success': success
	}, context_instance=RequestContext(request))

