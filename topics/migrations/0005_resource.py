# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 21:09
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0012_auto_20170112_1408'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students_group', '0003_auto_20170119_1543'),
        ('topics', '0004_auto_20170118_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('brief_description', models.TextField(blank=True, verbose_name='Brief Description')),
                ('show_window', models.BooleanField(default=False, verbose_name='Show in new window')),
                ('all_students', models.BooleanField(default=False, verbose_name='All Students')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('order', models.PositiveSmallIntegerField(null=True, verbose_name='Order')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('groups', models.ManyToManyField(blank=True, related_name='resource_groups', to='students_group.StudentsGroup', verbose_name='Groups')),
                ('students', models.ManyToManyField(blank=True, related_name='resource_students', to=settings.AUTH_USER_MODEL, verbose_name='Students')),
                ('tags', models.ManyToManyField(blank=True, related_name='resource_tags', to='subjects.Tag', verbose_name='Markers')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_topic', to='topics.Topic', verbose_name='Topic')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
