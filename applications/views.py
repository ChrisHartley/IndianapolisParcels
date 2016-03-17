from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotAllowed, JsonResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core import serializers
from django.core.serializers.json import Serializer
#from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.utils.encoding import is_protected_type
import os
from django.forms import inlineformset_factory


from .forms import ApplicationForm
#from user_files.forms import UploadedFileForm
from .models import Application
from property_inventory.models import Property
from applicants.models import ApplicantProfile
from user_files.models import UploadedFile
from django.contrib.auth.models import User


# used to send confirmation email
from django.core.mail import send_mail
from django.template.loader import render_to_string

from pprint import pprint


from django.views.generic import DetailView

@login_required
def process_application(request, action, id=None):
    if action == 'edit':
        app = get_object_or_404(Application, id=id, user=request.user)
        if app.frozen == True:
            return HttpResponse("This application has been submitted and can not be editted. To unfreeze this application email chris.hartley@renewindianapolis.org.", status=403)
        form = ApplicationForm(instance=app, user=request.user, id=app.pk)
    if action == 'new':
        # see if they already have an application with initial status, if so use that one again, if not create one.
        # Problem - multiple browser windows, or multiple browsers (eg start app on phone, continue on computer, then save phone app before computer app,
        # they share an ID and will overwrite each other. So not doing this for now. We'll see if it is a problem having a blank app saved for each app start
        # try:
        # 	app = Application.objects.get(user.request=user, status=Application.INITIAL_STATUS).first()
        # except model.DoesNotExist:
        # 	app = Application(user=request.user, status=Application.INITIAL_STATUS)
        # 	app.save()
        app = Application(user=request.user, status=Application.INITIAL_STATUS)
        app.save()
        form = ApplicationForm(instance=app, user=request.user, id=app.pk)
    if action == 'save':
        if request.method != 'POST':
            return HttpResponseNotAllowed('Error - POST required to save')
        app = get_object_or_404(Application, id=id, user=request.user)
        if app.frozen == True:
            return HttpResponse("This application has been submitted and can not be editted. To unfreeze this application email chris.hartley@renewindianapolis.org.", status=403)
        form = ApplicationForm(request.POST, request.FILES,
                               user=request.user, instance=app, id=app.pk)
        if form.is_valid():
            application = form.save(commit=False)
            if application.status == Application.INITIAL_STATUS:
                application.status = Application.ACTIVE_STATUS
            save_for_later = request.POST.get('save_for_later')
            if not save_for_later:  # they want to submit the application
                if form.validate_for_submission(id=application.id):
                    #application.frozen = True
                    application.status = Application.COMPLETE_STATUS
                    application.save()
                    applicant_email = request.user.email
                    property_address = app.Property
                    msg_plain = render_to_string('email/application_submitted.txt', {
                        'user': request.user.first_name,
                        'Property': property_address,
                    }
                    )
                    send_mail(
                        'Application received: {0}'.format(property_address),
                        msg_plain,
                        'info@renewindianapolis.org',
                        [applicant_email],
                    )
                    return HttpResponseRedirect(reverse('application_confirmation', args=(id,)))
                else:
                    "*!*!* validate_for_submission() returned false"

            application.frozen = False
            application.save()

    uploaded_files_sow = UploadedFile.objects.filter(
        user=request.user, application=app.id, file_purpose=UploadedFile.PURPOSE_SOW)
    uploaded_files_pof = UploadedFile.objects.filter(
        user=request.user, application=app.id, file_purpose=UploadedFile.PURPOSE_POF)
    uploaded_files_all = UploadedFile.objects.filter(
        user=request.user, application=app.id)

    return render_to_response('application.html', {
        'form': form,
        'app_id': app.id,
        'uploaded_files_sow': uploaded_files_sow,
        'uploaded_files_pof': uploaded_files_pof,
        'uploaded_files_all': uploaded_files_all,
        'title': 'application',
    }, context_instance=RequestContext(request))




# no longer needed since switching to admin app instead of home rolled dataTables
class DisplayNameJsonSerializer(Serializer):

    def handle_field(self, obj, field):
        value = field._get_val_from_obj(obj)
        display_method = "get_%s_display" % field.name
        if hasattr(obj, display_method):
            self._current[field.name] = getattr(obj, display_method)()
        elif is_protected_type(value):
            self._current[field.name] = value
        else:
            self._current[field.name] = field.value_to_string(obj)

# @staff_member_required
# def admin_view_application(request, id):
#     app = get_object_or_404(Application, id=id)
#     print app
#     applicant = app.user
#     print applicant
#     applicant_profile = get_object_or_404(ApplicantProfile, user=applicant)
#     print applicant_profile
#     form = ApplicationForm(instance=app, user=applicant, id=app.pk)
#     print "form.is_bound: ",form.is_bound
#     print "errors here:", form.errors
#     print form.is_valid()
#     if form.is_valid():
#         saved_form = form.save(commit=False)
#         blah = form.validate_for_submission(id=saved_form.id)
#         print blah
#     else:
#         print "errors", form.errors
#     return render(request, 'application_view.html', {'application': app, 'applicant': applicant, 'applicant_profile': applicant_profile})

@login_required
def application_confirmation(request, id):
    app = get_object_or_404(Application, id=id, user=request.user)
    return render(request, 'confirmation.html', {
        'title': 'thank you',
        'Property': app.Property,
    })

class ApplicationDetail(DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'application_display.html'

class ApplicationDisplay(DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'application_detail.html'
