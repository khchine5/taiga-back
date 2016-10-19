# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0004_auto_20150202_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhooklog',
            name='duration',
            field=models.FloatField(verbose_name='duration', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webhooklog',
            name='request_data',
            field=django.contrib.postgres.fields.JSONField(verbose_name='request data'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webhooklog',
            name='request_headers',
            field=django.contrib.postgres.fields.JSONField(verbose_name='request headers', default={}),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webhooklog',
            name='response_data',
            field=models.TextField(verbose_name='response data'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webhooklog',
            name='response_headers',
            field=django.contrib.postgres.fields.JSONField(verbose_name='response headers', default={}),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webhooklog',
            name='status',
            field=models.IntegerField(verbose_name='status code'),
            preserve_default=True,
        ),
    ]
