# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_job_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
