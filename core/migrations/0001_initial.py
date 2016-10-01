# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-01 16:02
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Action',
                'verbose_name_plural': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='Action_Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action', verbose_name='Action_Applied')),
            ],
            options={
                'verbose_name': 'Action_Resource',
                'verbose_name_plural': 'Action_Resources',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time of action')),
                ('action_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action_Resource', verbose_name='Action_Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Actor')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time of action')),
                ('action_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action_Resource', verbose_name='Action_Resource')),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_Performer', to=settings.AUTH_USER_MODEL, verbose_name='Perfomer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_Actor', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('url', models.CharField(default='', max_length=100, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.AddField(
            model_name='action_resource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Resource', verbose_name='Resource'),
        ),
    ]
