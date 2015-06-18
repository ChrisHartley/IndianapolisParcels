# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='streetAddress',
            field=models.CharField(help_text=b'Supports partial matching, so you can enter either the full street address (eg 1425 E 11TH ST) to find one property or just the street name (eg 11th st) to find all the properties on that street.', max_length=255, verbose_name=b'Street Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='structureType',
            field=models.CharField(help_text=b'As classified by the Assessor', max_length=255, null=True, verbose_name=b'Structure Type', blank=True),
            preserve_default=True,
        ),
    ]
