# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-15 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Material')),
                ('link_url', models.URLField(verbose_name='Link_URL')),
                ('link_description', models.CharField(max_length=200, verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='links/')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
            bases=('courses.material',),
        ),
    ]
