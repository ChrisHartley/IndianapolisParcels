from django.contrib import admin
from .models import Application
from user_files.models import UploadedFile

from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    fields = ('file_purpose', 'file_purpose_other_explanation', 'file_download',)
    readonly_fields = ('file_download',)
    extra = 0

    def file_download(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("download_file", kwargs={'id':obj.id}),
                "Download"
            ))
        #return mark_safe("<a href='download link'>download link</a>")

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('modified','Property', 'user_link', 'organization','application_type','status')
    list_filter = ('status','application_type')
    search_fields = ('Property__parcel', 'Property__streetAddress', 'user__email', 'user__first_name', 'user__last_name', 'organization__name')
    readonly_fields = ('created', 'modified', 'user_readable', 'property_type', 'property_status','property_nsp','property_sidelot')
    fieldsets = (
        (None, {
            'fields': ( ('user','user_readable','organization'), ('created', 'modified'), ('Property', 'property_type','property_status','property_nsp','property_sidelot'), 'status')

        }),
        ('Qualifying Questions', {
            'fields': ( ('conflict_board_rc', 'conflict_board_rc_name'), 'active_citations', 'prior_tax_foreclosure', 'tax_status_of_properties_owned', 'other_properties_names_owned')
        }),
        ('Application Details', {
            'fields': ('application_type','planned_improvements','estimated_cost','source_of_financing','is_rental','nsp_income_qualifier','long_term_ownership','timeline')

        }),
        ('Staff fields', {
            'classes': ('collapse',),
            'fields': ('staff_summary','staff_pof_total',('staff_recommendation','staff_recommendation_notes','frozen'))

        })

    )
    inlines = [ UploadedFileInline ]
    def user_readable(self, obj):
        return obj.user.first_name + " " + obj.user.last_name + " - " + obj.user.email

    def property_type(self, obj):
        return obj.Property.structureType

    def property_nsp(self, obj):
        return obj.Property.nsp

    def property_sidelot(self, obj):
        return obj.Property.sidelot_eligible

    def property_status(self, obj):
        return obj.Property.status

    def user_link(self, obj):
       return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:applicants_applicantprofile_change", args=(obj.user.profile.id,)),
                obj.user.first_name + ' ' + obj.user.last_name + ' - ' + obj.user.email
            ))
    user_link.short_description = 'user'

admin.site.register(Application, ApplicationAdmin)
