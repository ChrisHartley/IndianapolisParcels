from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotAllowed, JsonResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core import serializers
from django.core.serializers.json import Serializer
#from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.utils.encoding import is_protected_type
import os
from django.forms import inlineformset_factory

# , ApplicationForm0,ApplicationForm1,ApplicationForm2,ApplicationForm3,ApplicationForm4,ApplicationForm5
from .forms import ApplicationForm, UploadedFileForm
from .models import UploadedFile, Application
from property_inventory.models import Property
from django.contrib.auth.models import User

# ajaxuploader requirements
from django.middleware.csrf import get_token  # not used?
from ajaxuploader.views import AjaxFileUploader

#from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage

# used to send confirmation email
from django.core.mail import send_mail
from django.template.loader import render_to_string

# used to save incomplete application in process
#import pickle

from pprint import pprint

import_uploader = AjaxFileUploader()


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


@login_required
def applications_asJson(request):
    json_serializer = DisplayNameJsonSerializer()
    json = json_serializer.serialize(Application.objects.exclude(
        status=Application.INITIAL_STATUS), use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')


@login_required
def applications_datatable(request):
    return render_to_response('admin_datatables.html', {
        'title': 'applications'
    }, context_instance=RequestContext(request))


@login_required
def application_confirmation(request, id):
    app = get_object_or_404(Application, id=id, user=request.user)
    return render(request, 'confirmation.html', {
        'title': 'thank you',
        'Property': app.Property,
    })

# APPLICATION_FORMS = [
#     ('QualifyingQuestions', ApplicationForm0),
#     ('PropertyAndApplicationType', ApplicationForm1),
#     ('EndBuyerAndUse', ApplicationForm2),
#     ('Improvements', ApplicationForm3),
#     ('Financing', ApplicationForm4),
#     ('Sidelot', ApplicationForm5),
# ]
#
#
# def standard_app_selected(wizard):
#     cleaned_data = wizard.get_cleaned_data_for_step('PropertyAndApplicationType') or {'application_type': 'none'}
#     return cleaned_data['application_type'] == Application.STANDARD
#
# def sidelot_app_selected(wizard):
#     cleaned_data = wizard.get_cleaned_data_for_step('PropertyAndApplicationType') or {'application_type': 'none'}
#     return cleaned_data['application_type'] == Application.SIDELOT
#
# def homestead_app_selected(wizard):
#     cleaned_data = wizard.get_cleaned_data_for_step('PropertyAndApplicationType') or {'application_type': 'none'}
#     return cleaned_data['application_type'] == Application.HOMESTEAD
#
#
# class ApplicationFormWizard(SessionWizardView):
#     form_list = APPLICATION_FORMS
#     location=os.path.join(settings.MEDIA_ROOT, 'applicants', 'files')
#     file_storage = FileSystemStorage(settings.MEDIA_ROOT)
#     template_name = 'application_steps.html'
#     instance = None
#     condition_dict={
#         'EndBuyerAndUse': standard_app_selected,
#         'Improvements': standard_app_selected or homestead_app_selected,
#         'Financing': standard_app_selected or homestead_app_selected,
#         'Sidelot': sidelot_app_selected,
#     }
#
#     # def get_form_initial(self, step):
#     #     initial = {}
#     #     print "in get_form_initial()"
#     #     try:
#     #         data = IncompleteApplication.objects.get(user=self.request.user)
#     #         print "loaded incompleteapplication"
#     #         unpickled_data = pickle.loads(data.postdata)
#     #         pprint(unpickled_data)
#     #         initial = unpickled_data['step_data']
#     #         #initial['']
#     #         #pprint(initial)
#     #         #pprint(initial['QualifyingQuestions'])
#     #
#     #     except:
#     #         pass
#     #     # if step in self.request.session['wizard_application_form_wizard']['step_data']:
#     #     #     pprint(self.request.session['wizard_application_form_wizard']['step_data'][step])
#     #     #     for key, value in self.request.session['wizard_application_form_wizard']['step_data'][step]:
#     #     #         initial[key] = value
#     #     #         print key,value
#     #     print "Step is:", step
#     #     try:
#     #         print "returning initial from saved data"
#     #         return self.initial_dict.get(step, initial[step])
#     #     except:
#     #         print "returning blank initial"
#     #         return self.initial_dict.get(step, {})
#     #     #return self.request.session['wizard_application_form_wizard']['step_data']
#     #
#     # def process_step(self, form):
#     #     try:
#     #         data = IncompleteApplication.objects.get(user=self.request.user)
#     #         print "loaded incompleteapplication"
#     #     except:
#     #         data = IncompleteApplication(user=self.request.user)
#     #         print "exception created incompleteapplication"
#     #     #for k,v in self.request.session:
#     #     #pprint(self.request.session['wizard_application_form_wizard'])
#     #
#     #     data.postdata=pickle.dumps(self.request.session['wizard_application_form_wizard']['step_data'])
#     #     data.save()
#     #     print "saved progress"
#     #     return self.get_form_step_data(form)
#
#     def get_form_instance(self, step):
#         if self.instance is None:
#             self.instance = Application(user=self.request.user)
#         return self.instance
#
#     def done(self, form_list, form_dict, **kwargs):
#         self.instance.save()
#         applicant_email = self.instance.user.email
#         property_address = form_dict['PropertyAndApplicationType'].cleaned_data['Property']
#         msg_plain = render_to_string('email/application_submitted.txt', {
#             'user': self.instance.user.first_name,
#             'Property': property_address,
#
#             }
#         )
#         send_mail(
#             'Application received: {0}'.format(property_address),
#             msg_plain,
#             'info@renewindianapolis.org',
#             [applicant_email],
#         )
#         # delete pickle for application in progress
#         IncompleteApplication.objects.get(user=self.request.user).delete()
#         return HttpResponseRedirect('/page-to-redirect-to-when-done/')
#
# application_form_wizard_view = ApplicationFormWizard.as_view()
#
# def ResumeApplicationFormWizard(request):
#     try:
#         prev_data = IncompleteApplication.objects.get(user=request.user)
#         print prev_data
#         #request.POST = pickle.loads(prev_data.postdata)
#         #s['wizard_application_form_wizard'] = pickle.loads(prev_data.postdata)
#         #s.save()
#         request.session['wizard_application_form_wizard']['step_data'] = pickle.loads(prev_data.postdata)
#
#     except:
#         raise Http404("Application does not exist")
#     #print application_form_wizard_view(request)
#     #return HttpResponseRedirect('/apply2/')
# return application_form_wizard_view(request,
# initial_dict=pickle.loads(prev_data.postdata))
