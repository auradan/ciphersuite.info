# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthAlgorithm',
            fields=[
                ('short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('long_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'authentication algorithm',
                'verbose_name_plural': 'authentication algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CipherSuite',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('hex_byte_1', models.CharField(max_length=4)),
                ('hex_byte_2', models.CharField(max_length=4)),
                ('auth_algorithm', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='directory.AuthAlgorithm', verbose_name='authentication algorithm')),
            ],
            options={
                'verbose_name': 'cipher suite',
                'verbose_name_plural': 'cipher suites',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EncAlgorithm',
            fields=[
                ('short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('long_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'encryption algorithm',
                'verbose_name_plural': 'encryption algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HashAlgorithm',
            fields=[
                ('short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('long_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'hash algorithm',
                'verbose_name_plural': 'hash algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KexAlgorithm',
            fields=[
                ('short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('long_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'key exchange algorithm',
                'verbose_name_plural': 'key exchange algorithms',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocolVersion',
            fields=[
                ('short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('long_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'protocol version',
                'verbose_name_plural': 'protocol versions',
                'ordering': ['short_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rfc',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('IST', 'Internet Standard'), ('PST', 'Proposed Standard'), ('DST', 'Draft Standard'), ('BCP', 'Best Current Practise'), ('INF', 'Informational'), ('EXP', 'Experimental'), ('HST', 'Historic'), ('UND', 'Undefined')], editable=False, max_length=3)),
                ('title', models.CharField(editable=False, max_length=250)),
                ('release_year', models.IntegerField(editable=False)),
                ('url', models.URLField(editable=False)),
                ('is_draft', models.BooleanField(default=False, editable=False)),
                ('defined_cipher_suites', models.ManyToManyField(blank=True, related_name='defining_rfcs', to='directory.CipherSuite', verbose_name='defined cipher suites')),
                ('related_documents', models.ManyToManyField(blank=True, related_name='_rfc_related_documents_+', to='directory.Rfc', verbose_name='related RFCs')),
            ],
            options={
                'verbose_name': 'RFC',
                'verbose_name_plural': 'RFCs',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=10000)),
                ('glyphicon', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'static page',
                'verbose_name_plural': 'static pages',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('severity', models.CharField(choices=[('HIG', 'High'), ('MED', 'Medium'), ('LOW', 'Low')], default='LOW', max_length=3)),
            ],
            options={
                'verbose_name': 'vulnerability',
                'verbose_name_plural': 'vulnerabilities',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='protocolversion',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='kexalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='hashalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='encalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='enc_algorithm',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='directory.EncAlgorithm', verbose_name='encryption algorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='hash_algorithm',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='directory.HashAlgorithm', verbose_name='hash algorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='kex_algorithm',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='directory.KexAlgorithm', verbose_name='key exchange algorithm'),
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='protocol_version',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='directory.ProtocolVersion', verbose_name='protocol version'),
        ),
        migrations.AddField(
            model_name='authalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AlterUniqueTogether(
            name='ciphersuite',
            unique_together=set([('hex_byte_1', 'hex_byte_2')]),
        ),
    ]
