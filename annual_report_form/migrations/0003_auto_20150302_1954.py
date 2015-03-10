# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annual_report_form', '0002_auto_20150302_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual_report',
            name='feedback',
            field=models.TextField(help_text=b'Do you have any other comments on your project or feedback for Renew Indianapolis about your experience with our program?', max_length=5120, verbose_name=b'Feedback'),
            preserve_default=True,
        ),
    ]
