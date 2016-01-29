# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicants', '0012_auto_20160127_1142'),
        ('applications', '0031_auto_20160127_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('supporting_document', models.FileField(max_length=512, upload_to=b'attachments/%Y/%m/%d')),
                ('file_purpose', models.IntegerField(choices=[(1, b'Scope of Work'), (2, b'Proof of Funds'), (3, b'Letter of Support'), (4, b'Elevation View'), (5, b'Schedule of Values'), (7, b'Authorization Form'), (9, b'Secretary of State Business Entity Report'), (10, b'IRS Determination Letter'), (11, b"Organization's Most Recent Financial Statement"), (8, b'Other')])),
                ('file_purpose_other_explanation', models.CharField(max_length=255, verbose_name=b'What is this file?', blank=True)),
                ('application', models.ForeignKey(to='applications.Application', null=True)),
                ('organization', models.ForeignKey(to='applicants.Organization', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
