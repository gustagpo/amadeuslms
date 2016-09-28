# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 20:27
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Resource')),
                ('limit_date', models.DateTimeField(verbose_name='Deliver Date')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
            bases=('core.resource',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('objectivies', models.TextField(blank=True, verbose_name='Objectivies')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('max_students', models.PositiveIntegerField(blank=True, verbose_name='Maximum Students')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('init_register_date', models.DateField(verbose_name='Register Date (Begin)')),
                ('end_register_date', models.DateField(verbose_name='Register Date (End)')),
                ('init_date', models.DateField(verbose_name='Begin of Course Date')),
                ('end_date', models.DateField(verbose_name='End of Course Date')),
                ('image', models.ImageField(blank=True, upload_to='courses/', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Category', verbose_name='Category')),
                ('professors', models.ManyToManyField(related_name='courses_professors', to=settings.AUTH_USER_MODEL, verbose_name='Professors')),
                ('students', models.ManyToManyField(related_name='courses_student', to=settings.AUTH_USER_MODEL, verbose_name='Students')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ('create_date', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Resource')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
            bases=('core.resource',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('init_date', models.DateField(verbose_name='Begin of Subject Date')),
                ('end_date', models.DateField(verbose_name='End of Subject Date')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of last update')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='courses.Course', verbose_name='Course')),
                ('professors', models.ManyToManyField(related_name='subjects', to=settings.AUTH_USER_MODEL, verbose_name='Professors')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'ordering': ('create_date', 'name'),
            },
        ),
        migrations.CreateModel(
            name='SubjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('subjects', models.ManyToManyField(to='courses.Subject')),
            ],
            options={
                'verbose_name': 'subject category',
                'verbose_name_plural': 'subject categories',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of last update')),
                ('visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
                'ordering': ('create_date', 'name'),
            },
        ),
        migrations.AddField(
            model_name='material',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='activity',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Topic', verbose_name='Topic'),
        ),
    ]
