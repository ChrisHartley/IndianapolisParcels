from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.utils.html import escape, escapejs


from .forms import ApplicantProfileForm, OrganizationForm
from .models import ApplicantProfile, Organization
from .tables import PropertyInquiryTable, ApplicationTable, OrganizationTable
from applications.models import Application
from property_inquiry.models import propertyInquiry


@login_required
def profile_home(request):
	try:
		property_inquiries = propertyInquiry.objects.filter(user=request.user)
		property_inquiries_table = PropertyInquiryTable(property_inquiries)
	except propertyInquiry.DoesNotExist:
		property_inquiries_table = None


	try:
		applications = Application.objects.filter(user=request.user)
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
			return HttpResponse('<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' % \
	        # escape() calls force_unicode.
				(escape(pending.pk), escapejs(pending)))
	else:
		orgForm = OrganizationForm()

	return render_to_response('create_organization.html', {
		'form': orgForm,
		'success': success,
		'title': "new organization"
	}, context_instance=RequestContext(request))

@login_required
def edit_organization(request):
	success = False
	if 'edit' in request.GET:
		try:
			organization = Organization.objects.get(id=request.GET['edit'])
		except Organization.DoesNotExist:
			organization = None
	if request.method == 'POST':
		orgForm = OrganizationForm(request.POST, request.FILES, instance=organization)
		if orgForm.is_valid():
			pending = orgForm.save(commit=False)
			pending.user = request.user
			pending.save()
			success = True
	else:
		orgForm = OrganizationForm()
	return render_to_response('create_profile.html', {
		'success': success,
		'profileForm': orgForm,
		'title': "new organization"
	}, context_instance=RequestContext(request))

@login_required
def show_organizations(request):
	organizations = Organization.objects.filter(user=request.user)

	return render_to_response('organizations.html', {
		'organizations': organizations,
		'title': "organizations"
	}, context_instance=RequestContext(request))
