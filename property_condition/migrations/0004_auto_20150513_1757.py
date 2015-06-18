# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_condition', '0003_auto_20150513_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionreport',
            name='doors',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='electrical_knob_tube_cloth',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='electrical_standard',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_brick',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_other',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_vinyl',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='exterior_siding_wood',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='fencing',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='flooring_covering',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='flooring_subflooring',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='foundation_crawl',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='foundation_slab',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='garage',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_air_conditioner',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_duct_work',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='hvac_furance',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='kitchen_cabinets',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='landscaping',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='plumbing_metal',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='plumbing_plastic',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_framing',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_gutters',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='roof_shingles',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='walls_drywall',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='walls_lathe_plaster',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
        migrations.AlterField(
            model_name='conditionreport',
            name='windows',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Good / Satisfactory'), (2, b'Fair / Repair'), (1, b'Poor / Replace'), (None, b'N/A')]),
        ),
    ]
