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


class UserAdmin(UserAdmin):
    inlines = (ApplicantProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Organization)
#admin.site.register(ApplicantProfile, ApplicantProfileAdmin)
