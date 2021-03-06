# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0003_overdue_removed'),
    ]

    operations = [
        migrations.AddField(
            model_name='overdue',
            name='cid',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Cedula'),
        ),
        migrations.AddField(
            model_name='overdue',
            name='residual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
