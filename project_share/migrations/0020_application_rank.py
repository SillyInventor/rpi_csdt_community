# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_share', '0019_auto_20170608_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='rank',
            field=models.IntegerField(default=100),
        ),
    ]