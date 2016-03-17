from django.contrib.gis import admin
from .models import Property, CDC

class PropertyAdmin(admin.OSMGeoAdmin):
    search_fields = ('parcel', 'streetAddress')
    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'
    modifiable = False


admin.site.register(Property, PropertyAdmin)
admin.site.register(CDC)
