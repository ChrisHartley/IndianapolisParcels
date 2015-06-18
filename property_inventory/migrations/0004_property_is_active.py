# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0003_auto_20150512_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_active',
            field=models.BooleanField(default=True, help_text=b'Is this property listing active?'),
        ),
    ]
