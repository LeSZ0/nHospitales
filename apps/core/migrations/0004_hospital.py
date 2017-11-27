# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171127_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Used to build hospital URL.', max_length=150, unique=True, verbose_name='Slug')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Up'), (2, 'Down')], default=1, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('city', models.ForeignKey(help_text='Hospital City', on_delete=django.db.models.deletion.CASCADE, to='core.City')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Hospitals',
                'verbose_name': 'Hospital',
            },
        ),
    ]