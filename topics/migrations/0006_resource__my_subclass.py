# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='_my_subclass',
            field=models.CharField(default='webpage', max_length=200),
            preserve_default=False,
        ),
    ]
