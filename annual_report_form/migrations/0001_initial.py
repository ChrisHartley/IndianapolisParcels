# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annual_report_form.models


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='annual_report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parcel', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=254)),
                ('organization', models.CharField(max_length=254, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('percent_completed', models.PositiveIntegerField(help_text=b'Roughly speaking, what percentage complete is this project?')),
                ('past_expenses', models.PositiveIntegerField(help_text=b'It is ok to use rough estimates.', verbose_name=b'Funds spent to date')),
                ('work_completed', models.TextField(help_text=b'What work has been completed?', max_length=5120, verbose_name=b'Written narative of the improvements made to date')),
                ('work_remaining', models.TextField(help_text=b'What work remains to be completed?', max_length=5120, verbose_name=b'Work remaining')),
                ('future_expenses', models.PositiveIntegerField(help_text=b'It is ok to use rough estimates.', verbose_name=b'Anticipated remaining expenses')),
                ('feedback', models.TextField(help_text=b'Do you have any other comments on your project or feedback for Renew Indianapolis about your experience with our program?', max_length=5120, verbose_name=b'Feedback')),
                ('certificate_of_completion_ready', models.BooleanField(default=False, verbose_name=b'Are you ready for a certificate of completion inspection?')),
                ('property_occupied', models.BooleanField(default=False, verbose_name=b'Is the property occupied?')),
                ('front_exterior_picture', models.ImageField(upload_to=annual_report_form.models.content_file_name, blank=True)),
                ('back_exterior_picture', models.ImageField(upload_to=annual_report_form.models.content_file_name, blank=True)),
                ('kitchen_picture', models.ImageField(upload_to=annual_report_form.models.content_file_name, blank=True)),
                ('bathroom_picture', models.ImageField(upload_to=annual_report_form.models.content_file_name, blank=True)),
                ('other_picture', models.ImageField(help_text=b'Project photo of your choice (optional)', upload_to=annual_report_form.models.content_file_name, blank=True)),
                ('Property', models.ForeignKey(blank=True, to='property_inventory.Property', null=True)),
            ],
        ),
    ]
