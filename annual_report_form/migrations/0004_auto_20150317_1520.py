# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annual_report_form.models


class Migration(migrations.Migration):

    dependencies = [
        ('annual_report_form', '0003_auto_20150302_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='annual_report',
            name='certificate_of_completion_ready',
            field=models.BooleanField(default=False, verbose_name=b'Are you ready for a certificate of completion inspection?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual_report',
            name='other_picture',
            field=models.ImageField(help_text=b'Project photo of your choice (optional)', upload_to=annual_report_form.models.content_file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual_report',
            name='property_occupied',
            field=models.BooleanField(default=False, verbose_name=b'Is the property occupied?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='future_expenses',
            field=models.PositiveIntegerField(help_text=b'It is ok to use rough estimates.', verbose_name=b'Anticipated remaining expenses'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='past_expenses',
            field=models.PositiveIntegerField(help_text=b'It is ok to use rough estimates.', verbose_name=b'Funds spent to date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annual_report',
            name='work_completed',
            field=models.TextField(help_text=b'What work has been completed?', max_length=5120, verbose_name=b'Written narative of the improvements made to date'),
            preserve_default=True,
        ),
    ]
