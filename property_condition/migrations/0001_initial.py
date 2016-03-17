# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import property_condition.models


class Migration(migrations.Migration):

    dependencies = [
        ('property_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=property_condition.models.content_file_name, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('roof_shingles', models.IntegerField(blank=True, null=True, verbose_name=b'Shingles', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('roof_shingles_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('roof_framing', models.IntegerField(blank=True, null=True, verbose_name=b'Framing', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('roof_framing_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('roof_gutters', models.IntegerField(blank=True, null=True, verbose_name=b'Gutters', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('roof_gutters_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('foundation_slab', models.IntegerField(blank=True, null=True, verbose_name=b'Slab', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('foundation_slab_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('foundation_crawl', models.IntegerField(blank=True, null=True, verbose_name=b'Crawlspace', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('foundation_crawl_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('exterior_siding_brick', models.IntegerField(blank=True, null=True, verbose_name=b'Brick', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_brick_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('exterior_siding_vinyl', models.IntegerField(blank=True, null=True, verbose_name=b'Vinyl', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_vinyl_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('exterior_siding_wood', models.IntegerField(blank=True, null=True, verbose_name=b'Wood', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_wood_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('exterior_siding_other', models.IntegerField(blank=True, null=True, verbose_name=b'Other', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('exterior_siding_other_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('windows', models.IntegerField(blank=True, null=True, verbose_name=b'Windows', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('windows_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('garage', models.IntegerField(blank=True, null=True, verbose_name=b'Garage', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('garage_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('fencing', models.IntegerField(blank=True, null=True, verbose_name=b'Fencing', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('fencing_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('landscaping', models.IntegerField(blank=True, null=True, verbose_name=b'Landscaping', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('landscaping_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('doors', models.IntegerField(blank=True, null=True, verbose_name=b'Doors', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('doors_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('kitchen_cabinets', models.IntegerField(blank=True, null=True, verbose_name=b'Kitchen Cabinets', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('kitchen_cabinets_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('flooring_subflooring', models.IntegerField(blank=True, null=True, verbose_name=b'Subflooring', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('flooring_subflooring_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('flooring_covering', models.IntegerField(blank=True, null=True, verbose_name=b'Covering', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('flooring_covering_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('electrical_knob_tube_cloth', models.IntegerField(blank=True, null=True, verbose_name=b'Knob, tube and cloth', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('electrical_knob_tube_cloth_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('electrical_standard', models.IntegerField(blank=True, null=True, verbose_name=b'Standard', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('electrical_standard_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('plumbing_metal', models.IntegerField(blank=True, null=True, verbose_name=b'Copper / metal', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('plumbing_metal_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('plumbing_plastic', models.IntegerField(blank=True, null=True, verbose_name=b'PVC / PEX', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('plumbing_plastic_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('walls_drywall', models.IntegerField(blank=True, null=True, verbose_name=b'Drywall', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('walls_drywall_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('walls_lathe_plaster', models.IntegerField(blank=True, null=True, verbose_name=b'Plaster and lathe', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('walls_lathe_plaster_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('hvac_furance', models.IntegerField(blank=True, null=True, verbose_name=b'Furnace', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('hvac_furance_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('hvac_duct_work', models.IntegerField(blank=True, null=True, verbose_name=b'Duct work', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('hvac_duct_work_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('hvac_air_conditioner', models.IntegerField(blank=True, null=True, verbose_name=b'AC', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')])),
                ('hvac_air_conditioner_notes', models.CharField(max_length=512, verbose_name=b'Notes', blank=True)),
                ('Property', models.ForeignKey(to='property_inventory.Property')),
            ],
        ),
    ]
