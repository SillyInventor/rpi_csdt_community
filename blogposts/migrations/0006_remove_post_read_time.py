# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0005_auto_20160412_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='read_time',
        ),
    ]
