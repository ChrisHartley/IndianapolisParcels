# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inquiry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyinquiry',
            name='showing_scheduled',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
