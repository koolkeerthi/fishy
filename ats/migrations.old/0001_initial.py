# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('board', models.CharField(choices=[('CBSE', 'CBSE'), ('ICSE', 'ICSE'), ('State Board Tamil', 'State Board'), ('State Board Matriculation', 'State Board Matriculation')], max_length=30)),
                ('address', models.TextField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(default='Tamil Nadu', editable=False, max_length=50)),
                ('country', models.CharField(default='India', editable=False, max_length=30)),
                ('phone1', models.CharField(max_length=30)),
                ('phone2', models.CharField(blank=True, max_length=30, null=True)),
                ('fax', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
