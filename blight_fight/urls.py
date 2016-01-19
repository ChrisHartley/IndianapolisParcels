from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

from neighborhood_associations.views import get_relevant_neighborhood_assocations
from applicants.views import edit_organization
#from applications.views import


urlpatterns = patterns('',
    url(r'admin/', include(admin.site.urls)),
    url(r'^$', 'applicants.views.profile_home', name='applicants_home'),
    url(r'test/$', 'property_inventory.views.show_all_properties'),

    url(r'lookup_street_address/$', 'property_inventory.views.getAddressFromParcel', name='get_address_from_parcel'),

    url(r'admin-inquiry-list/$', 'property_inquiry.views.inquiry_list'),

	url(r'property_inquiry/thanks/(?P<id>[0-9]+)$', 'property_inquiry.views.property_inquiry_confirmation', name='property_inquiry_confirmation'),
    url(r'property_inquiry/$', 'property_inquiry.views.submitPropertyInquiry', name='submit_property_inquiry'),

	url(r'search-neighborhood-association/$', get_relevant_neighborhood_assocations.as_view() ),
	url(r'search-neighborhood-association/(?P<parcel>[0-9]{7})/$', get_relevant_neighborhood_assocations.as_view() ),

	url(r'application_status/$', 'property_inventory.views.showApplications'),

	url(r'search_property/$', 'property_inventory.views.searchProperties'),
	#url(r'propertiesJSON/$', 'property_inventory.views.propertiesAsJSON',  name='properties_ajax_url'),
	url(r'propertyPopup/$', 'property_inventory.views.propertyPopup'),

	url(r'admin-condition-report/$', 'property_condition.views.condition_report_list'),
	url(r'condition_report/$', 'property_condition.views.submitConditionReport'),

	url(r'annual-report/$', 'annual_report_form.views.showAnnualReportForm'),
	url(r'view_annual_report/(?P<id>[0-9]+)/$', 'annual_report_form.views.showAnnualReportData', name='view_annual_report'),
	url(r'admin_annual_report/$', 'annual_report_form.views.showAnnualReportIndex'),

	url(r'json_applications$', 'applications.views.applications_asJson', name='applications_ajax'),
	url(r'admin_applications$', TemplateView.as_view(template_name="admin_datatables.html")),

	url(r'accounts/profile$', 'applicants.views.profile_home', name='applicants_home'),
	url(r'accounts/profile/edit$', 'applicants.views.showApplicantProfileForm', name='applicants_profile'),
    url(r'accounts/organization/new/$', edit_organization.as_view(), name='applicants_organization_add'),
    url(r'accounts/organization/edit/(?P<id>\w+)/$', edit_organization.as_view(), name='applicants_organization_edit'),
	url(r'accounts/organization$', 'applicants.views.show_organizations', name='applicants_organization'),

	#url(r'map/accounts/', include('allauth.urls')), #django all-auth
	url(r'accounts/', include('allauth.urls')), #django all-auth

	url(r'application/delete_file/$', 'applications.views.delete_uploaded_file', name='uploadedfile_delete'),
	url(r'application/upload_file/$', 'applications.views.import_uploader', name='my_ajax_upload'),
	url(r'application/thanks/(?P<id>[0-9]+)$', 'applications.views.application_confirmation', name='application_confirmation'),

	url(r'application/(?P<action>\w+)/$', 'applications.views.process_application', name='process_application'),
	url(r'application/(?P<action>\w+)/(?P<id>[0-9]+)/$', 'applications.views.process_application', name='process_application'),



)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
