# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('house_no', models.CharField(max_length=8)),
                ('flat_no', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='people',
            field=models.ManyToManyField(to='contacts.Person'),
        ),
        migrations.AddField(
            model_name='email',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person'),
        ),
    ]
