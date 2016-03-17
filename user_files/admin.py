from django.contrib import admin
from .models import UploadedFile
# Register your models here.
class UploadedFileAdmin(admin.ModelAdmin):
    model = UploadedFile
    list_display = ('user','organization','application','supporting_document')

admin.site.register(UploadedFile,UploadedFileAdmin)
