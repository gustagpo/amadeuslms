# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MymeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=100, unique=True, verbose_name='Type')),
                ('icon', models.CharField(max_length=50, unique=True, verbose_name='Icon')),
            ],
            options={
                'verbose_name_plural': 'Amadeus Myme Types',
                'verbose_name': 'Amadeus Myme Type',
            },
        ),
    ]
