# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('mailing_address_line1', models.CharField(max_length=b'100')),
                ('mailing_address_line2', models.CharField(max_length=b'100', blank=True)),
                ('mailing_address_line3', models.CharField(max_length=b'100', blank=True)),
                ('mailing_address_city', models.CharField(max_length=b'100')),
                ('mailing_address_state', models.CharField(max_length=b'100')),
                ('mailing_address_zip', models.CharField(max_length=b'100')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('mailing_address_line1', models.CharField(max_length=b'100')),
                ('mailing_address_line2', models.CharField(max_length=b'100', blank=True)),
                ('mailing_address_line3', models.CharField(max_length=b'100', blank=True)),
                ('mailing_address_city', models.CharField(max_length=b'100')),
                ('mailing_address_state', models.CharField(max_length=b'100')),
                ('mailing_address_zip', models.CharField(max_length=b'100')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
