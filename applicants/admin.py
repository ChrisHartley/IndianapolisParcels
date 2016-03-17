from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ApplicantProfile, Organization


class ApplicantProfileInline(admin.StackedInline):
    model = ApplicantProfile
    can_delete = False
    verbose_name_plural = 'profile'

# class ApplicantProfileAdmin(admin.ModelAdmin):
    #search_fields = ('organization', 'phone_number','mailing_address_line1','mailing_address_line2','mailing_address_line3')

class OrganizationInline(admin.TabularInline):
    model = Organization
    extra = 0

class SimpleUserInline(admin.TabularInline):
    model = User
    extra = 0
    inlines = [OrganizationInline]

class ApplicantProfileAdmin(admin.ModelAdmin):
    model = ApplicantProfile
    readonly_fields = ('user_email', 'user_first_name', 'user_last_name')
    list_display = ('user_email', 'user_first_name', 'user_last_name', 'phone_number', 'mailing_address_line1', 'mailing_address_line2', 'mailing_address_line3', 'mailing_address_city', 'mailing_address_state', 'mailing_address_zip')
    fields = ('user_email', 'user_first_name', 'user_last_name', 'phone_number', 'mailing_address_line1', 'mailing_address_line2', 'mailing_address_line3', 'mailing_address_city', 'mailing_address_state', 'mailing_address_zip')
    #inlines = [OrganizationInline]

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    def user_email(self, obj):
        return obj.user.email


class UserAdmin(UserAdmin):
    inlines = (ApplicantProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Organization)
admin.site.register(ApplicantProfile, ApplicantProfileAdmin)
#admin.site.register(ApplicantProfile, ApplicantProfileAdmin)
