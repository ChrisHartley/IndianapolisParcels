from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django_tables2_reports.config import RequestConfigReport as RequestConfig

from PIL import Image

from property_inventory.models import Property
from .models import ConditionReport
from .forms import ConditionReportForm
from .filters import ConditionReportFilters
from .tables import ConditionReportTable


# Displays form template for property inquiry submissions, and saves those submissions
@login_required
def submitConditionReport(request):
	parcelNumber = False
	success = False
	if request.method == 'POST':
		form = ConditionReportForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			success = True
	form = ConditionReportForm()
	return render_to_response('condition_report.html', {
		'form': form,
		'title': 'condition report',
		'success': success
	}, context_instance=RequestContext(request))

# Displays submitted property inquiries
@login_required
def condition_report_list(request):
	config = RequestConfig(request)
	f = ConditionReportFilters(request.GET, queryset=ConditionReport.objects.all())
	table = ConditionReportTable(f)
	config.configure(table)
	return render_to_response('admin-with-filter-table.html', {
		'filter': f,
		'title': 'Condition Reports Admin',
		'table': table
	}, context_instance=RequestContext(request))
