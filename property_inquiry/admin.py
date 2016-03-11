from django.contrib import admin
from .models import propertyInquiry
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class propertyInquiryAdmin(admin.ModelAdmin):
    list_display = ('Property', 'user_name', 'user_phone', 'showing_scheduled', 'timestamp')
    #fields =
    search_fields = ('Property__parcel', 'Property__streetAddress', 'user__email', 'user__first_name', 'user__last_name')
    readonly_fields = ('applicant_ip_address','timestamp')

    def user_name(self, obj):
        email_link = '<a target="_blank" href="https://mail.google.com/a/landbankofindianapolis.org/mail/u/1/?view=cm&fs=1&to={0}&su={1}&body={2}&tf=1">{3}</a>'.format(obj.user.email, 'Property visit: '+str(obj.Property), 'Hi ' +obj.user.first_name+',', obj.user.email)
        name_link = '<a href="{}">{}</a>'.format(
             reverse("admin:applicants_applicantprofile_change", args=(obj.user.profile.id,)),
                 obj.user.first_name + ' ' + obj.user.last_name
             )
        return mark_safe(name_link + ' - ' + email_link)
    user_name.short_description = 'user'

    def user_phone(self, obj):
        return obj.user.profile.phone_number


admin.site.register(propertyInquiry, propertyInquiryAdmin)
