from django.contrib import admin
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('parcel', 'streetAddress')

admin.site.register(Property, PropertyAdmin)
