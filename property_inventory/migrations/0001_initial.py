# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('CDCtype', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('propertyType', models.CharField(max_length=2, verbose_name=b'property type', choices=[(b'lb', b'Landbank'), (b'sp', b'County Owned Surplus')])),
                ('parcel', models.CharField(help_text=b'The 7 digit local parcel number for a property, ex 1052714', unique=True, max_length=7, verbose_name=b'parcel number')),
                ('streetAddress', models.CharField(help_text=b'Supports partial matching, so you can enter either the full street address (eg 1425 E 11TH ST) to find one property or just the street name (eg 11th st) to find all the properties on that street.', max_length=255, verbose_name=b'Street Address')),
                ('nsp', models.BooleanField(default=False, help_text=b'If a property comes with requirements related to the Neighborhood Stabilization Program.', verbose_name=b'NSP')),
                ('quiet_title_complete', models.BooleanField(default=False, help_text=b'If quiet title process has been completed.', verbose_name=b'Quiet Title Complete')),
                ('structureType', models.CharField(help_text=b'As classified by the Assessor', max_length=255, null=True, verbose_name=b'Structure Type', blank=True)),
                ('urban_garden', models.BooleanField(default=False, help_text=b'If the property is currently licensed as an urban garden through the Office of Sustainability')),
                ('status', models.CharField(help_text=b"The property's status with Renew Indianapolis", max_length=255, null=True, blank=True)),
                ('sidelot_eligible', models.BooleanField(default=False, help_text=b'If the property is currently elgibile for the side-lot program')),
                ('price', models.DecimalField(help_text=b'The price of the property', null=True, max_digits=8, decimal_places=2)),
                ('area', models.FloatField(help_text=b'The parcel area in square feet')),
                ('applicant', models.CharField(help_text=b'Name of current applicant for status page', max_length=255, null=True)),
                ('homestead_only', models.BooleanField(default=False, help_text=b'Only available for homestead applications')),
                ('bep_demolition', models.BooleanField(default=False, help_text=b'Slated for demolition under the Blight Elimination Program', verbose_name=b'Slated for BEP demolition')),
                ('project_agreement_released', models.BooleanField(default=False, help_text=b'Has the project agreement on a sold property been released?')),
                ('is_active', models.BooleanField(default=True, help_text=b'Is this property listing active?')),
                ('price_obo', models.BooleanField(default=False, help_text=b'Price is Or Best Offer')),
                ('cdc', models.ForeignKey(blank=True, to='property_inventory.CDC', help_text=b'The Community Development Corporation boundries the property falls within.', null=True, verbose_name=b'CDC')),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zoning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='property',
            name='zipcode',
            field=models.ForeignKey(blank=True, to='property_inventory.Zipcode', help_text=b'The zipcode of the property', null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='zone',
            field=models.ForeignKey(blank=True, to='property_inventory.Zoning', help_text=b'The zoning of the property', null=True),
        ),
    ]
