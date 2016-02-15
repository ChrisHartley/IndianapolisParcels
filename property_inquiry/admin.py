from django.contrib import admin
from .models import propertyInquiry

class propertyInquiryAdmin(admin.ModelAdmin):
    fields = ('Property', 'user.email', 'timestamp')
    
admin.site.register(propertyInquiry, propertyInquiryAdmin)
