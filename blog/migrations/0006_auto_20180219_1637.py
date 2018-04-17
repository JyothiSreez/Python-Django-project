# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 00:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='activation_key',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='author',
            name='email_validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
