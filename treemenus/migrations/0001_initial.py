# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'navigation',
                'verbose_name_plural': 'navigation',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50, verbose_name='caption')),
                ('url', models.CharField(blank=True, max_length=200, verbose_name='URL')),
                ('named_url', models.CharField(blank=True, max_length=200, verbose_name='named URL')),
                ('level', models.IntegerField(default=0, editable=False, verbose_name='level')),
                ('rank', models.IntegerField(default=0, editable=False, verbose_name='rank')),
                ('menu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contained_items', to='treemenus.Menu', verbose_name='menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treemenus.MenuItem', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='root_item',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_root_item_of', to='treemenus.MenuItem', verbose_name='root item'),
        ),
    ]
