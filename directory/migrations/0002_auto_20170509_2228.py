# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfc',
            name='status',
            field=models.CharField(choices=[('Internet Standard', 'Internet Standard'), ('Proposed Standard', 'Proposed Standard'), ('Draft Standard', 'Draft Standard'), ('Best Current Practise', 'Best Current Practise'), ('Informational', 'Informational'), ('Experimental', 'Experimental'), ('Historic', 'Historic')], max_length=25),
        ),
    ]