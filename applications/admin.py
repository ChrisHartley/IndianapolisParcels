from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    #    search_fields = ('parcel', 'streetAddress')
    pass

admin.site.register(Application, ApplicationAdmin)
