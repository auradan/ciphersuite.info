# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20171120_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciphersuite',
            name='gnutls_name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='ciphersuite',
            name='openssl_name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
