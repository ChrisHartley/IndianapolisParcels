# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annual_report_form.models


class Migration(migrations.Migration):

    dependencies = [
        ('annual_report_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual_report',
            name='back_exterior_picture',
            field=models.ImageField(upload_to=annual_report_form.models.content_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='bathroom_picture',
            field=models.ImageField(upload_to=annual_report_form.models.content_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='front_exterior_picture',
            field=models.ImageField(upload_to=annual_report_form.models.content_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='future_expenses',
            field=models.PositiveIntegerField(help_text=b'It is ok to use rough estimates.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='kitchen_picture',
            field=models.ImageField(upload_to=annual_report_form.models.content_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='past_expenses',
            field=models.PositiveIntegerField(help_text=b'It is ok to use rough estimates.'),
            preserve_default=True,
        ),
    ]
