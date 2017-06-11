# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 02:50
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
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('backendversion', models.IntegerField(blank=True, db_column='BackendVersion', null=True, verbose_name='backend version')),
                ('frontendversion', models.IntegerField(blank=True, db_column='FrontendVersion', null=True, verbose_name='frontend version')),
            ],
            options={
                'verbose_name': 'current version',
                'verbose_name_plural': 'current versions',
                'managed': True,
                'db_table': 'CurrentVersion',
            },
        ),
        migrations.CreateModel(
            name='LookupActivity',
            fields=[
                ('activity', models.CharField(db_column='Activity', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
                'managed': True,
                'db_table': 'LookupActivity',
            },
        ),
        migrations.CreateModel(
            name='LookupAuthorType',
            fields=[
                ('authortype', models.CharField(db_column='AuthorType', max_length=50, primary_key=True, serialize=False, verbose_name='author type')),
            ],
            options={
                'verbose_name': 'author type',
                'verbose_name_plural': 'author types',
                'managed': True,
                'db_table': 'LookupAuthorType',
            },
        ),
        migrations.CreateModel(
            name='LookupCustomaryUse',
            fields=[
                ('usedfor', models.CharField(db_column='UsedFor', max_length=255, primary_key=True, serialize=False, verbose_name='used_for')),
            ],
            options={
                'verbose_name': 'customary use',
                'verbose_name_plural': 'customary uses',
                'managed': True,
                'db_table': 'LookupCustomaryUse',
            },
        ),
        migrations.CreateModel(
            name='LookupHabitat',
            fields=[
                ('habitat', models.CharField(db_column='Habitat', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'habitat',
                'verbose_name_plural': 'habitats',
                'managed': True,
                'db_table': 'LookupHabitat',
            },
        ),
        migrations.CreateModel(
            name='LookupLocalityType',
            fields=[
                ('localitytype', models.CharField(db_column='LocalityType', max_length=255, primary_key=True, serialize=False, verbose_name='locality type')),
            ],
            options={
                'verbose_name': 'locality type',
                'verbose_name_plural': 'locality types',
                'managed': True,
                'db_table': 'LookupLocalityType',
            },
        ),
        migrations.CreateModel(
            name='LookupMediaType',
            fields=[
                ('mediatype', models.CharField(db_column='MediaType', max_length=255, primary_key=True, serialize=False, verbose_name='type')),
                ('mediacategory', models.CharField(blank=True, db_column='MediaCategory', max_length=255, null=True, verbose_name='category')),
            ],
            options={
                'verbose_name': 'media type',
                'verbose_name_plural': 'media types',
                'managed': True,
                'db_table': 'LookupMediaType',
            },
        ),
        migrations.CreateModel(
            name='LookupParticipants',
            fields=[
                ('participants', models.CharField(db_column='Participants', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'participant',
                'verbose_name_plural': 'participants',
                'managed': True,
                'db_table': 'LookupParticipants',
            },
        ),
        migrations.CreateModel(
            name='LookupPartUsed',
            fields=[
                ('partused', models.CharField(db_column='PartUsed', max_length=255, primary_key=True, serialize=False, verbose_name='part used')),
            ],
            options={
                'verbose_name': 'part used',
                'verbose_name_plural': 'parts used',
                'managed': True,
                'db_table': 'LookupPartUsed',
            },
        ),
        migrations.CreateModel(
            name='LookupPlanningUnit',
            fields=[
                ('planningunitid', models.AutoField(db_column='PlanningUnitID', primary_key=True, serialize=False)),
                ('planningunitname', models.CharField(blank=True, db_column='PlanningUnitName', max_length=100, null=True, verbose_name='planning unit')),
            ],
            options={
                'verbose_name': 'planning unit',
                'verbose_name_plural': 'planning units',
                'managed': True,
                'db_table': 'LookupPlanningUnit',
            },
        ),
        migrations.CreateModel(
            name='LookupReferenceType',
            fields=[
                ('documenttype', models.CharField(db_column='DocumentType', max_length=25, primary_key=True, serialize=False, verbose_name='document type')),
            ],
            options={
                'verbose_name': 'reference type',
                'verbose_name_plural': 'reference types',
                'managed': True,
                'db_table': 'LookupReferenceType',
            },
        ),
        migrations.CreateModel(
            name='LookupResourceGroup',
            fields=[
                ('resourceclassificationgroup', models.CharField(db_column='ResourceClassificationGroup', max_length=255, primary_key=True, serialize=False, verbose_name='broad species group')),
            ],
            options={
                'verbose_name': 'resource group',
                'verbose_name_plural': 'resource groups',
                'managed': True,
                'db_table': 'LookupResourceGroup',
            },
        ),
        migrations.CreateModel(
            name='LookupSeason',
            fields=[
                ('season', models.CharField(db_column='Season', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'season',
                'verbose_name_plural': 'seasons',
                'managed': True,
                'db_table': 'LookupSeason',
            },
        ),
        migrations.CreateModel(
            name='LookupTechniques',
            fields=[
                ('techniques', models.CharField(db_column='Techniques', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'technique',
                'verbose_name_plural': 'techniques',
                'managed': True,
                'db_table': 'LookupTechniques',
            },
        ),
        migrations.CreateModel(
            name='LookupTiming',
            fields=[
                ('timing', models.CharField(db_column='Timing', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'timing',
                'verbose_name_plural': 'timings',
                'managed': True,
                'db_table': 'LookupTiming',
            },
        ),
        migrations.CreateModel(
            name='LookupTribe',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tribeunit', models.CharField(blank=True, db_column='TribeUnit', max_length=50, null=True, verbose_name='tribe subunit')),
                ('tribe', models.CharField(blank=True, db_column='Tribe', max_length=100, null=True, verbose_name='tribe')),
                ('federaltribe', models.CharField(blank=True, db_column='FederalTribe', max_length=100, null=True, verbose_name='tribal government')),
            ],
            options={
                'verbose_name': 'tribe',
                'verbose_name_plural': 'tribes',
                'managed': True,
                'db_table': 'LookupTribe',
            },
        ),
        migrations.CreateModel(
            name='LookupUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=100, null=True, verbose_name='username')),
                ('usingcustomusername', models.BooleanField(db_column='UsingCustomUsername', default=False, verbose_name='using custom username')),
                ('usertitle', models.CharField(blank=True, db_column='UserTitle', max_length=100, null=True, verbose_name='title')),
                ('useraffiliation', models.CharField(blank=True, db_column='UserAffiliation', max_length=100, null=True, verbose_name='affiliation')),
            ],
            options={
                'verbose_name': 'user info',
                'verbose_name_plural': 'user info',
                'managed': True,
                'db_table': 'LookupUserInfo',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('personid', models.AutoField(db_column='PersonID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=255, null=True, verbose_name='first name')),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True, verbose_name='last name')),
                ('yearborn', models.IntegerField(blank=True, db_column='YearBorn', null=True, verbose_name='year born')),
                ('village', models.CharField(blank=True, db_column='Village', max_length=255, null=True)),
                ('relationshiptootherpeople', models.TextField(blank=True, db_column='RelationshipToOtherPeople', null=True, verbose_name='relationship to other people')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
                'managed': True,
                'db_table': 'People',
            },
        ),
    ]