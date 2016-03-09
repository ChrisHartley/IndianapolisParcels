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
    inlines = [ UploadedFileInline ]
    def user_link(self, obj):
       return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:applicants_applicantprofile_change", args=(obj.user.profile.id,)),
                obj.user.first_name + ' ' + obj.user.last_name + ' - ' + obj.user.email
            ))
    user_link.short_description = 'user'

admin.site.register(Application, ApplicationAdmin)
