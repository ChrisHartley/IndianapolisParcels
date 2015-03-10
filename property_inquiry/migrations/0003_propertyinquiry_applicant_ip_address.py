# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inquiry', '0002_propertyinquiry_showing_scheduled'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyinquiry',
            name='applicant_ip_address',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
