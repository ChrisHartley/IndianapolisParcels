# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.CharField(max_length=b'255', null=True, blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{7,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('mailing_address_line1', models.CharField(max_length=b'100')),
                ('mailing_address_line2', models.CharField(max_length=b'100', blank=True)),
                ('mailing_address_line3', models.CharField(max_length=b'100', blank=True)),
                ('mailing_address_city', models.CharField(max_length=b'100')),
                ('mailing_address_state', models.CharField(max_length=b'100')),
                ('mailing_address_zip', models.CharField(max_length=b'100')),
                ('conflict_board_rc', models.BooleanField(verbose_name=b"Do you, any partner/member of your entity, or any of your entity's board members serve on the Renew Indianapolis Board of Directors or Committees and thus pose a potential conflict of interest?")),
                ('conflict_board_rc_name', models.CharField(max_length=255, verbose_name=b'If yes, what is their name?', blank=True)),
                ('tax_status_of_properties_owned', models.IntegerField(help_text=b"If you do not own any real property (real estate) in Marion County chose N/A. If you chose 'Unknown' we will contact you for an explanation", verbose_name=b'Tax status of real property owned in Marion County', choices=[(3, b'Current'), (2, b'Delinquent'), (1, b'Unknown'), (None, b'N/A - No real property owned')])),
                ('other_properties_names_owned', models.CharField(max_length=b'255', verbose_name=b'If you own properties under other names or are a partner/member of an entity that owns properties, please list the names of those entities here')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='applicantuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='applicantuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='ApplicantUser',
        ),
    ]
