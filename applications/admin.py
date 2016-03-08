from django.contrib import admin
from .models import Application
from user_files.models import UploadedFile

class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    extra = 1


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('modified','Property', 'get_user', 'organization','application_type','status')
    list_filter = ('status','application_type')
    search_fields = ('Property__parcel', 'Property__streetAddress', 'user__email', 'user__first_name', 'user__last_name')
    inlines = [ UploadedFileInline]
    def get_user(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name + ' - ' + obj.user.email

admin.site.register(Application, ApplicationAdmin)
