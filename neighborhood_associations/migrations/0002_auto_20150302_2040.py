# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood_associations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood_association',
            name='area2',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
