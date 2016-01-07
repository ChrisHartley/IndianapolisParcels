from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.utils.html import escape, escapejs
from django.views.generic import View
from django.core.urlresolvers import reverse




from .forms import ApplicantProfileForm, OrganizationForm
from .models import ApplicantProfile, Organization
from .tables import PropertyInquiryTable, ApplicationTable, OrganizationTable
from applications.models import Application
from property_inquiry.models import propertyInquiry


@login_required
def profile_home(request):
	try:
		property_inquiries = propertyInquiry.objects.filter(user=request.user).order_by('-timestamp')
		property_inquiries_table = PropertyInquiryTable(property_inquiries)
	except propertyInquiry.DoesNotExist:
		property_inquiries_table = None


	try:
		applications = Application.objects.filter(user=request.user).order_by('-modified')
		applications_table = ApplicationTable(applications)
	except Application.DoesNotExist:
		applications_table = None


	try:
		profile = ApplicantProfile.objects.get(user=request.user)
	except ApplicantProfile.DoesNotExist:
		profile = None

	try:
		organizations = Organization.objects.filter(user=request.user)
		organizations_table = OrganizationTable(organizations)
	except Organization.DoesNotExist:
		organizations_table = None

	return render_to_response('profile_home.html', {
		'property_inquiries': property_inquiries_table,
		'applications': applications_table,
		'organizations': organizations_table,
		'profile': profile,
		'title': "home"
	}, context_instance=RequestContext(request))

@login_required
def showApplicantProfileForm(request):
	success = False
	try:
		profile = ApplicantProfile.objects.get(user=request.user)
	except ApplicantProfile.DoesNotExist:
		profile = None

	if request.method == 'POST':
		ProfileForm = ApplicantProfileForm(request.POST, request.FILES, instance=profile)
		if ProfileForm.is_valid():
			pending = ProfileForm.save(commit=False)
			pending.user = request.user
			pending.save()
			success = True
	else:
		ProfileForm = ApplicantProfileForm(instance=profile)
	return render_to_response('create_profile.html', {
		'profileForm': ProfileForm,
		'title': "edit profile",
		'success': success
	}, context_instance=RequestContext(request))

@login_required
def add_organization_popup(request):
	success = False
	if request.method == 'POST':
		orgForm = OrganizationForm(request.POST, request.FILES)
		if orgForm.is_valid():
			pending = orgForm.save(commit=False)
			pending.user = request.user
			pending.save()
			return HttpResponse('<html><body><script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script></body></html>' % (escape(pending.pk), escapejs(pending)))
	else:
		orgForm = OrganizationForm()

	return render_to_response('create_organization.html', {
		'form': orgForm,
		'success': success,
		'title': "new organization"
	}, context_instance=RequestContext(request))


class edit_organization(View):
	def get(self, request, id):
		organization = get_object_or_404(Organization, id=id, user=request.user)
		form = OrganizationForm(instance=organization)
		return render(request, 'edit_organization.html', {'title': 'edit organization', 'form': form})

	def post(self, request, id):
		organization = get_object_or_404(Organization, id=id, user=request.user)
		form = OrganizationForm(request.POST, request.FILES, instance=organization)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect(reverse('applicants_organization'))
		else:
			return render(request, 'edit_organization.html', {'title': 'edit organization', 'form': form})

@login_required
def show_organizations(request):
	organizations = Organization.objects.filter(user=request.user).order_by('name')
	organizations_table = OrganizationTable(organizations)
	return render_to_response('organizations.html', {
		'organizations': organizations,
		'table': organizations_table,
		'title': "organizations"
	}, context_instance=RequestContext(request))
