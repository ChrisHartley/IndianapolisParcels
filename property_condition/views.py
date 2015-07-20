from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

from django_tables2_reports.config import RequestConfigReport as RequestConfig

from property_inquiry.models import propertyInquiry
from property_inventory.models import Property
from property_condition.models import ConditionReport
from property_condition.forms import ConditionReportForm
from property_condition.filters import ConditionReportFilters
from property_condition.tables import ConditionReportTable

# Displays form template for property condition submissions, and saves those submissions
@user_passes_test(lambda u: u.groups.filter(name='City Staff').exists() or u.is_staff)
def submitConditionReport(request):
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

# Displays submitted property condition reports
#@user_passes_test(lambda u: u.groups.filter(name='City Staff').exists() or u.is_staff)
def condition_report_list(request):
	config = RequestConfig(request)
	f = ConditionReportFilters(request.GET, queryset=propertyInquiry.objects.all().order_by('-timestamp'))
	table = ConditionReportTable(f)
	config.configure(table)
	return render_to_response('admin-with-filter-table.html', {
		'filter': f,
		'title': 'Condition Reports Admin',
		'table': table
	}, context_instance=RequestContext(request))
