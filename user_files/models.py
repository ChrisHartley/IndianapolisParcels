from django.db import models
import pyclamd
from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.signals import file_uploaded
from django.dispatch import receiver

import os
from django.conf import settings

from django.contrib.auth.models import User

from applicants.models import Organization
from applications.models import Application

def virus_scan(input_file):
    try:
        cd = pyclamd.ClamdUnixSocket()
        # test if server is reachable
        cd.ping()
    except pyclamd.ConnectionError:
        # if failed, test for network socket
        cd = pyclamd.ClamdNetworkSocket()
    try:
        cd.ping()
    except pyclamd.ConnectionError:
        raise ValueError('could not connect to clamd server either by unix or network socket')

    scan_results = cd.scan_file(input_file)
    if scan_results is not None:
        print 'Virus found:', scan_results[0]
        return True
    else:
        return False

class UploadedFile(models.Model):
    PURPOSE_SOW = 1
    PURPOSE_POF = 2
    PURPOSE_LOS = 3
    PURPOSE_ELEVATION_VIEW = 4
    PURPOSE_SCHEDULE_OF_VALUES = 5
    PURPOSE_OTHER = 6
    PURPOSE_AUTHORIZATION_FORM = 7
    PURPOSE_OTHER = 8
    PURPOSE_SOS_ENTITY_REPORT = 9
    PURPOSE_IRS_DETERMINATION_LETTER = 10
    PURPOSE_MOST_RECENT_FINANCIAL_STATEMENT = 11

    FILE_PURPOSE_CHOICES = (
        (PURPOSE_SOW, 'Scope of Work'),
        (PURPOSE_POF, 'Proof of Funds'),
        (PURPOSE_LOS, 'Letter of Support'),
        (PURPOSE_ELEVATION_VIEW, 'Elevation View'),
        (PURPOSE_SCHEDULE_OF_VALUES, 'Schedule of Values'),
        (PURPOSE_AUTHORIZATION_FORM, 'Authorization Form'),
        (PURPOSE_SOS_ENTITY_REPORT, 'Secretary of State Business Entity Report'),
        (PURPOSE_IRS_DETERMINATION_LETTER, 'IRS Determination Letter'),
        (PURPOSE_MOST_RECENT_FINANCIAL_STATEMENT,
            "Organization's Most Recent Financial Statement"),
         (PURPOSE_OTHER, 'Other')

    )
    user = models.ForeignKey(User)
    organization = models.ForeignKey(Organization, null=True)
    application = models.ForeignKey(Application, null=True)
    created = models.DateTimeField(auto_now_add=True)
    supporting_document = models.FileField(
        upload_to="attachments/%Y/%m/%d", max_length=512)
    file_purpose = models.IntegerField(choices=FILE_PURPOSE_CHOICES)
    file_purpose_other_explanation = models.CharField(
        verbose_name='What is this file?',
        blank=True,
        max_length=255
    )

    def __unicode__(self):
        return os.path.basename(self.supporting_document.name)

    @receiver(file_uploaded, sender=AjaxFileUploader)
    def create_on_upload(sender, backend, request, **kwargs):
        if virus_scan(backend.path):
            # should delete or otherwise quarantine uploaded file
            print 'returning in virus_scan called from create_on_upload'
            return

        try:
            app = Application.objects.get(id=request.GET.get('application'))
        except Application.DoesNotExist:
            app = None
        try:
            org = Organization.objects.get(id=request.GET.get('organization'))
        except Organization.DoesNotExist:
            org = None

        new_path = os.path.join(
            settings.MEDIA_ROOT, request.user.email, os.path.basename(backend.path))
        dst_dir = os.path.join(settings.MEDIA_ROOT, request.user.email)
        basename = os.path.basename(new_path)
        head, tail = os.path.splitext(basename)
        dst_file = os.path.join(dst_dir, basename)

        count = 0
        while os.path.exists(dst_file):
            count += 1
            dst_file = os.path.join(dst_dir, '%s-%d%s' % (head, count, tail))

        os.renames(backend.path, dst_file)
        UploadedFile.objects.create(file_purpose=request.GET[
                                    'file_purpose'], supporting_document=new_path, user=request.user, organization=org, application=app)
