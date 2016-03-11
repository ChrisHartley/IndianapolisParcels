from django.contrib.gis import admin
from .models import Property, CDC

class PropertyAdmin(admin.OSMGeoAdmin):
    search_fields = ('parcel', 'streetAddress')


admin.site.register(Property, PropertyAdmin)
admin.site.register(CDC)
