# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20170609_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='flat_no',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
