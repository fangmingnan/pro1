# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ly', '0002_delete_liuyanku'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiuYanKu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
