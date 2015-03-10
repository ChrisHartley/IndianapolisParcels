from django.conf.urls import patterns, include, url
from django.contrib import admin

from neighborhood_associations.views import get_relevant_neighborhood_assocations


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'renew_indianapolis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'annual_report/$', 'annual_report_form.views.showAnnualReportForm'),
	url(r'lookup_street_address/$', 'property_inventory.views.getAddressFromParcel'),
	url(r'lookup_possible_street_addresses/$', 'property_inventory.views.getMatchingAddresses'),
	url(r'admin-inquiry-list/$', 'property_inquiry.views.inquiry_list'),
	url(r'property-inquiry/$', 'property_inquiry.views.submitPropertyInquiry'),
	url(r'search-neighborhood-association/$', get_relevant_neighborhood_assocations.as_view() ),
)
