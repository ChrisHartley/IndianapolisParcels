from django.shortcuts import render, get_object_or_404
from ajaxuploader.views import AjaxFileUploader
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import os, tempfile, zipfile
from django.http import HttpResponse, JsonResponse
from django.core.servers.basehttp import FileWrapper
import mimetypes
from .models import UploadedFile

@staff_member_required
def send_file(request, id):
    """
    https://www.djangosnippets.org/snippets/365/
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    requested_file = get_object_or_404(UploadedFile, id=id)
    filename = str(requested_file.supporting_document.name)
    wrapper = FileWrapper(open(filename,'rb'))
    content_type = mimetypes.MimeTypes().guess_type(filename)[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(filename))
    return response

import_uploader = AjaxFileUploader()

@login_required
def delete_uploaded_file(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Error - POST required to delete')
    file_id = request.POST.get('file_id', None)
    selected_file = get_object_or_404(
        UploadedFile, id=file_id, user=request.user)

    protected = False
    message = 'File deleted.'
    if selected_file.application is not None:
        if selected_file.application.frozen == True:
            protected = True
            message = 'The application this file is linked to is frozen for editing and so the file can not be deleted. Email chris.hartley@renewindianapolis.org for help.'

    data = {
        "name": selected_file.supporting_document.name,
        "id": selected_file.id,
        "protected": protected,
        "message": message
        }

    if protected == False:
        selected_file.delete()
    return JsonResponse(data)
