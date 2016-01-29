from django.shortcuts import render
from ajaxuploader.views import AjaxFileUploader
from django.contrib.auth.decorators import login_required
from .models import UploadedFile

# Create your views here.
import_uploader = AjaxFileUploader()

@login_required
def delete_uploaded_file(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Error - POST required to delete')
    file_id = request.POST.get('file_id', None)
    selected_file = get_object_or_404(
        UploadedFile, id=file_id, user=request.user)
    data = {"name": selected_file.supporting_document.name, "id": selected_file.id}
    selected_file.delete()
    return JsonResponse(data)
