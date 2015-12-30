from django.contrib import admin
from .models import Application, UploadedFile


class ApplicationAdmin(admin.ModelAdmin):
#    search_fields = ('parcel', 'streetAddress')
    pass

admin.site.register(Application, ApplicationAdmin)
admin.site.register(UploadedFile)
