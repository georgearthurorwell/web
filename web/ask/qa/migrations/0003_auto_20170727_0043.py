# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 21:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20170727_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default='x', on_delete=django.db.models.deletion.CASCADE, related_name='question_author', to=settings.AUTH_USER_MODEL),
        ),
    ]