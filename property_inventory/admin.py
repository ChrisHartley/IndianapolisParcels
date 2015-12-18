from django.contrib import admin
from .models import Property, CDC


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('parcel', 'streetAddress')

admin.site.register(Property, PropertyAdmin)
admin.site.register(CDC)
