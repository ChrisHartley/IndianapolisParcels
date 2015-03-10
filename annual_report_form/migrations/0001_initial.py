# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('past_expenses', models.PositiveIntegerField()),
                ('work_completed', models.TextField(help_text=b'What work has been completed?', max_length=5120, verbose_name=b'Work completed')),
                ('work_remaining', models.TextField(help_text=b'What work remains to be completed?', max_length=5120, verbose_name=b'Work remaining')),
                ('future_expenses', models.PositiveIntegerField()),
                ('feedback', models.TextField(help_text=b'Do you have any feedback for Renew Indianapolis about your experience with our program?', max_length=5120, verbose_name=b'Feedback')),
                ('front_exterior_picture', models.ImageField(upload_to=b'annual_report_images/%Y/%m/%d')),
                ('back_exterior_picture', models.ImageField(upload_to=b'annual_report_images/%Y/%m/%d')),
                ('kitchen_picture', models.ImageField(upload_to=b'annual_report_images/%Y/%m/%d')),
                ('bathroom_picture', models.ImageField(upload_to=b'annual_report_images/%Y/%m/%d')),
                ('Property', models.ForeignKey(blank=True, to='property_inventory.Property', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
