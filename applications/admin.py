from django.contrib import admin
from .models import Application
from user_files.models import UploadedFile

class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    extra = 0


class ApplicationAdmin(admin.ModelAdmin):
    #    search_fields = ('parcel', 'streetAddress')
    inlines = [ UploadedFileInline]

admin.site.register(Application, ApplicationAdmin)
