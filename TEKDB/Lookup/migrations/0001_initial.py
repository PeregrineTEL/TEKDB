# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentVersion',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('backendversion', models.IntegerField(blank=True, db_column='backendversion', null=True, verbose_name='backend version')),
                ('frontendversion', models.IntegerField(blank=True, db_column='frontendversion', null=True, verbose_name='frontend version')),
            ],
            options={
                'db_table': 'currentversion',
                'verbose_name': 'current version',
                'managed': True,
                'verbose_name_plural': 'current versions',
            },
        ),
        migrations.CreateModel(
            name='LookupActivity',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('activity', models.CharField(db_column='activity', max_length=255)),
            ],
            options={
                'db_table': 'lookupactivity',
                'verbose_name': 'activity',
                'managed': True,
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='LookupAuthorType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('authortype', models.CharField(db_column='authortype', max_length=50, verbose_name='author type')),
            ],
            options={
                'db_table': 'lookupauthortype',
                'verbose_name': 'author type',
                'managed': True,
                'verbose_name_plural': 'author types',
            },
        ),
        migrations.CreateModel(
            name='LookupCustomaryUse',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('usedfor', models.CharField(db_column='usedfor', max_length=255, verbose_name='used_for')),
            ],
            options={
                'db_table': 'lookupcustomaryuse',
                'verbose_name': 'customary use',
                'managed': True,
                'verbose_name_plural': 'customary uses',
            },
        ),
        migrations.CreateModel(
            name='LookupHabitat',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('habitat', models.CharField(db_column='habitat', max_length=100)),
            ],
            options={
                'db_table': 'lookuphabitat',
                'verbose_name': 'habitat',
                'managed': True,
                'verbose_name_plural': 'habitats',
            },
        ),
        migrations.CreateModel(
            name='LookupLocalityType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('localitytype', models.CharField(db_column='localitytype', max_length=255, verbose_name='locality type')),
            ],
            options={
                'db_table': 'lookuplocalitytype',
                'verbose_name': 'locality type',
                'managed': True,
                'verbose_name_plural': 'locality types',
            },
        ),
        migrations.CreateModel(
            name='LookupMediaType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('mediatype', models.CharField(db_column='mediatype', max_length=255, verbose_name='type')),
                ('mediacategory', models.CharField(blank=True, db_column='mediacategory', max_length=255, null=True, verbose_name='category')),
            ],
            options={
                'db_table': 'lookupmediatype',
                'verbose_name': 'media type',
                'managed': True,
                'verbose_name_plural': 'media types',
            },
        ),
        migrations.CreateModel(
            name='LookupParticipants',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('participants', models.CharField(db_column='participants', max_length=255)),
            ],
            options={
                'db_table': 'lookupparticipants',
                'verbose_name': 'participant',
                'managed': True,
                'verbose_name_plural': 'participants',
            },
        ),
        migrations.CreateModel(
            name='LookupPartUsed',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('partused', models.CharField(db_column='partused', max_length=255, verbose_name='part used')),
            ],
            options={
                'db_table': 'lookuppartused',
                'verbose_name': 'part used',
                'managed': True,
                'verbose_name_plural': 'parts used',
            },
        ),
        migrations.CreateModel(
            name='LookupPlanningUnit',
            fields=[
                ('planningunitid', models.AutoField(db_column='planningunitid', primary_key=True, serialize=False)),
                ('planningunitname', models.CharField(blank=True, db_column='planningunitname', max_length=100, null=True, verbose_name='planning unit')),
            ],
            options={
                'db_table': 'lookupplanningunit',
                'verbose_name': 'planning unit',
                'managed': True,
                'verbose_name_plural': 'planning units',
            },
        ),
        migrations.CreateModel(
            name='LookupReferenceType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('documenttype', models.CharField(db_column='documenttype', max_length=25, verbose_name='document type')),
            ],
            options={
                'db_table': 'lookupreferencetype',
                'verbose_name': 'reference type',
                'managed': True,
                'verbose_name_plural': 'reference types',
            },
        ),
        migrations.CreateModel(
            name='LookupResourceGroup',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('resourceclassificationgroup', models.CharField(db_column='resourceclassificationgroup', max_length=255, verbose_name='broad species group')),
            ],
            options={
                'db_table': 'lookupresourcegroup',
                'verbose_name': 'resource group',
                'managed': True,
                'verbose_name_plural': 'resource groups',
            },
        ),
        migrations.CreateModel(
            name='LookupSeason',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('season', models.CharField(db_column='season', max_length=255)),
            ],
            options={
                'db_table': 'lookupseason',
                'verbose_name': 'season',
                'managed': True,
                'verbose_name_plural': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='LookupTechniques',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('techniques', models.CharField(db_column='techniques', max_length=255)),
            ],
            options={
                'db_table': 'lookuptechniques',
                'verbose_name': 'technique',
                'managed': True,
                'verbose_name_plural': 'techniques',
            },
        ),
        migrations.CreateModel(
            name='LookupTiming',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('timing', models.CharField(db_column='timing', max_length=255)),
            ],
            options={
                'db_table': 'lookuptiming',
                'verbose_name': 'timing',
                'managed': True,
                'verbose_name_plural': 'timings',
            },
        ),
        migrations.CreateModel(
            name='LookupTribe',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('tribeunit', models.CharField(blank=True, db_column='tribeunit', max_length=50, null=True, verbose_name='tribe subunit')),
                ('tribe', models.CharField(blank=True, db_column='tribe', max_length=100, null=True, verbose_name='tribe')),
                ('federaltribe', models.CharField(blank=True, db_column='federaltribe', max_length=100, null=True, verbose_name='tribal government')),
            ],
            options={
                'db_table': 'lookuptribe',
                'verbose_name': 'tribe',
                'managed': True,
                'verbose_name_plural': 'tribes',
            },
        ),
        migrations.CreateModel(
            name='LookupUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, db_column='username', max_length=100, null=True, verbose_name='username')),
                ('usingcustomusername', models.BooleanField(db_column='usingcustomusername', default=False, verbose_name='using custom username')),
                ('usertitle', models.CharField(blank=True, db_column='usertitle', max_length=100, null=True, verbose_name='title')),
                ('useraffiliation', models.CharField(blank=True, db_column='useraffiliation', max_length=100, null=True, verbose_name='affiliation')),
            ],
            options={
                'db_table': 'lookupuserinfo',
                'verbose_name': 'user info',
                'managed': True,
                'verbose_name_plural': 'user info',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('personid', models.AutoField(db_column='personid', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstname', max_length=255, null=True, verbose_name='first name')),
                ('lastname', models.CharField(blank=True, db_column='lastname', max_length=255, null=True, verbose_name='last name')),
                ('village', models.CharField(blank=True, db_column='village', max_length=255, null=True)),
                ('yearborn', models.IntegerField(blank=True, db_column='yearborn', null=True, verbose_name='year born')),
                ('relationshiptootherpeople', models.TextField(blank=True, db_column='relationshiptootherpeople', null=True, verbose_name='relationship to other people')),
            ],
            options={
                'db_table': 'people',
                'verbose_name': 'person',
                'managed': True,
                'verbose_name_plural': 'people',
            },
        ),
    ]
