# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 21:40
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('-added_at',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-added_at',)},
        ),
        migrations.AlterModelManagers(
            name='question',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
