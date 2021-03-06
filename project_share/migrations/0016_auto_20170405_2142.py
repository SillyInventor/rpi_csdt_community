# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 01:42
from __future__ import unicode_literals

from django.db import migrations
import project_share.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_share', '0015_auto_20170405_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='when_requested',
            field=project_share.models.AutoDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='approval',
            name='when_updated',
            field=project_share.models.AutoDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='when_created',
            field=project_share.models.AutoDateTimeField(verbose_name=b'Created'),
        ),
        migrations.AlterField(
            model_name='project',
            name='when_modified',
            field=project_share.models.AutoDateTimeField(verbose_name=b'Last Changed'),
        ),
    ]
