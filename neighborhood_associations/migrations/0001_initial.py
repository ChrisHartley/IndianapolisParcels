# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood_Association',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('contact_first_name', models.CharField(max_length=255)),
                ('contact_last_name', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('contact_email_address', models.CharField(max_length=255)),
                ('last_updated', models.DateField()),
                ('area2', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
