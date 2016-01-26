from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry


class Overlay(models.Model):
    name = models.CharField(max_length=255)
    geometry = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    @property
    def area(self):
        return GEOSGeometry(self.geometry).area

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        abstract = True


class Neighborhood_Association(Overlay):
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_email_address = models.CharField(max_length=255)
    last_updated = models.DateField()
    area2 = models.FloatField()
