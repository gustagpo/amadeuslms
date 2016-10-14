# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_answersstudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersstudent',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_stundet', to='poll.Poll', verbose_name='Poll'),
        ),
    ]
