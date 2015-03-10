# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='propertyInquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parcel', models.CharField(max_length=7)),
                ('applicant_name', models.CharField(max_length=255)),
                ('applicant_email_address', models.EmailField(max_length=75)),
                ('applicant_phone', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Property', models.ForeignKey(blank=True, to='property_inventory.Property', null=True)),
            ],
            options={
                'verbose_name_plural': 'property inquiries',
            },
            bases=(models.Model,),
        ),
    ]
