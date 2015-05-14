from django.contrib.gis import admin

from .models import Neighborhood_Association

admin.site.register(Neighborhood_Association, admin.OSMGeoAdmin)

