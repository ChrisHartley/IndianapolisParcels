# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0002_auto_20150317_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='project_agreement_released',
            field=models.BooleanField(default=False, help_text=b'Has the project agreement on a sold property been released?'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bep_demolition',
            field=models.BooleanField(default=False, help_text=b'Slated for demolition under the Blight Elimination Program', verbose_name=b'Slated for BEP demolition'),
        ),
    ]
