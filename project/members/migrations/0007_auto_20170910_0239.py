# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20170908_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='emails',
            field=models.ManyToManyField(blank=True, null=True, to='rolodex.Email'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phones',
            field=models.ManyToManyField(blank=True, null=True, to='rolodex.Phone'),
        ),
    ]