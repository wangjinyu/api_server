# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170712_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='integer_id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='int_id',
            field=models.CharField(blank=True, default='', max_length=8),
        ),
    ]
