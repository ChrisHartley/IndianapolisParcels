# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_condition', '0004_auto_20150513_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionreport',
            name='doors',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Doors', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='doors_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='electrical_knob_tube_cloth',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Knob, tube and cloth', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='electrical_knob_tube_cloth_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='electrical_standard',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Standard', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='electrical_standard_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_brick',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Brick', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_brick_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_other',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Other', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_other_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_vinyl',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Vinyl', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_vinyl_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_wood',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Wood', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_wood_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='fencing',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Fencing', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='fencing_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='flooring_covering',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Covering', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='flooring_covering_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='flooring_subflooring',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Subflooring', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='flooring_subflooring_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='foundation_crawl',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Crawlspace', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='foundation_crawl_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='foundation_slab',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Slab', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='foundation_slab_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='garage',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Garage', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='garage_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_air_conditioner',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'AC', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_air_conditioner_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_duct_work',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Duct work', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_duct_work_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_furance',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Furnace', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_furance_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='kitchen_cabinets',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Kitchen Cabinets', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='kitchen_cabinets_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='landscaping',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Landscaping', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='landscaping_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='plumbing_metal',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Copper / metal', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='plumbing_metal_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='plumbing_plastic',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'PVC / PEX', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='plumbing_plastic_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_framing',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Framing', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_framing_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_gutters',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Gutters', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_gutters_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_shingles',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Shingles', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_shingles_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='walls_drywall',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Drywall', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='walls_drywall_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='walls_lathe_plaster',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Plaster and lathe', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='walls_lathe_plaster_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='windows',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Windows', choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='windows_notes',
            field=models.CharField(max_length=512, verbose_name=b'Notes', blank=True),
        ),
    ]
