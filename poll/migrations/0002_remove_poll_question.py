# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='question',
        ),
    ]
