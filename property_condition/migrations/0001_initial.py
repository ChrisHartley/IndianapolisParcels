# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0003_auto_20150512_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roof_shingles', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('roof_shingles_notes', models.CharField(max_length=512, blank=True)),
                ('roof_framing', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('roof_framing_notes', models.CharField(max_length=512, blank=True)),
                ('roof_gutters', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('roof_gutters_notes', models.CharField(max_length=512, blank=True)),
                ('foundation_slab', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('foundation_slab_notes', models.CharField(max_length=512, blank=True)),
                ('foundation_crawl', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('foundation_crawl_notes', models.CharField(max_length=512, blank=True)),
                ('exterior_siding_brick', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_brick_notes', models.CharField(max_length=512, blank=True)),
                ('exterior_siding_vinyl', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_vinyl_notes', models.CharField(max_length=512, blank=True)),
                ('exterior_siding_wood', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_wood_notes', models.CharField(max_length=512, blank=True)),
                ('exterior_siding_other', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_other_notes', models.CharField(max_length=512, blank=True)),
                ('windows', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('windows_notes', models.CharField(max_length=512, blank=True)),
                ('garage', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('garage_notes', models.CharField(max_length=512, blank=True)),
                ('fencing', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('fencing_notes', models.CharField(max_length=512, blank=True)),
                ('landscaping', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('landscaping_notes', models.CharField(max_length=512, blank=True)),
                ('doors', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('doors_notes', models.CharField(max_length=512, blank=True)),
                ('kitchen_cabinets', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('kitchen_cabinets_notes', models.CharField(max_length=512, blank=True)),
                ('flooring_subflooring', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('flooring_subflooring_notes', models.CharField(max_length=512, blank=True)),
                ('flooring_covering', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('flooring_covering_notes', models.CharField(max_length=512, blank=True)),
                ('electrical_knob_tube_cloth', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('electrical_knob_tube_cloth_notes', models.CharField(max_length=512, blank=True)),
                ('electrical_standard', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('electrical_standard_notes', models.CharField(max_length=512, blank=True)),
                ('plumbing_metal', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('plumbing_metal_notes', models.CharField(max_length=512, blank=True)),
                ('plumbing_plastic', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('plumbing_plastic_notes', models.CharField(max_length=512, blank=True)),
                ('walls_drywall', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('walls_drywall_notes', models.CharField(max_length=512, blank=True)),
                ('walls_lathe_plaster', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('walls_lathe_plaster_notes', models.CharField(max_length=512, blank=True)),
                ('hvac_furance', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('hvac_furance_notes', models.CharField(max_length=512, blank=True)),
                ('hvac_duct_work', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('hvac_duct_work_notes', models.CharField(max_length=512, blank=True)),
                ('hvac_air_conditioner', models.IntegerField(choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('hvac_air_conditioner_notes', models.CharField(max_length=512, blank=True)),
                ('Property', models.ForeignKey(to='property_inventory.Property')),
            ],
        ),
    ]
