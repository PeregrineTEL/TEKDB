# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 18:17
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
                'verbose_name_plural': 'current versions',
                'db_table': 'CurrentVersion',
                'verbose_name': 'current version',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupActivity',
            fields=[
                ('activity', models.CharField(db_column='Activity', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'activities',
                'db_table': 'LookupActivity',
                'verbose_name': 'activity',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupAuthorType',
            fields=[
                ('authortype', models.CharField(db_column='AuthorType', max_length=50, primary_key=True, serialize=False, verbose_name='author type')),
            ],
            options={
                'verbose_name_plural': 'author types',
                'db_table': 'LookupAuthorType',
                'verbose_name': 'author type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupCustomaryUse',
            fields=[
                ('usedfor', models.CharField(db_column='UsedFor', max_length=255, primary_key=True, serialize=False, verbose_name='used_for')),
            ],
            options={
                'verbose_name_plural': 'customary uses',
                'db_table': 'LookupCustomaryUse',
                'verbose_name': 'customary use',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupHabitat',
            fields=[
                ('habitat', models.CharField(db_column='Habitat', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'habitats',
                'db_table': 'LookupHabitat',
                'verbose_name': 'habitat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupLocalityType',
            fields=[
                ('localitytype', models.CharField(db_column='LocalityType', max_length=255, primary_key=True, serialize=False, verbose_name='locality type')),
            ],
            options={
                'verbose_name_plural': 'locality types',
                'db_table': 'LookupLocalityType',
                'verbose_name': 'locality type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupMediaType',
            fields=[
                ('mediatype', models.CharField(db_column='MediaType', max_length=255, primary_key=True, serialize=False, verbose_name='type')),
                ('mediacategory', models.CharField(blank=True, db_column='MediaCategory', max_length=255, null=True, verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'media types',
                'db_table': 'LookupMediaType',
                'verbose_name': 'media type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupParticipants',
            fields=[
                ('participants', models.CharField(db_column='Participants', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'participants',
                'db_table': 'LookupParticipants',
                'verbose_name': 'participant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupPartUsed',
            fields=[
                ('partused', models.CharField(db_column='PartUsed', max_length=255, primary_key=True, serialize=False, verbose_name='part used')),
            ],
            options={
                'verbose_name_plural': 'parts used',
                'db_table': 'LookupPartUsed',
                'verbose_name': 'part used',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupPlanningUnit',
            fields=[
                ('planningunitid', models.AutoField(db_column='PlanningUnitID', primary_key=True, serialize=False)),
                ('planningunitname', models.CharField(blank=True, db_column='PlanningUnitName', max_length=100, null=True, verbose_name='planning unit')),
            ],
            options={
                'verbose_name_plural': 'planning units',
                'db_table': 'LookupPlanningUnit',
                'verbose_name': 'planning unit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupReferenceType',
            fields=[
                ('documenttype', models.CharField(db_column='DocumentType', max_length=25, primary_key=True, serialize=False, verbose_name='document type')),
            ],
            options={
                'verbose_name_plural': 'reference types',
                'db_table': 'LookupReferenceType',
                'verbose_name': 'reference type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupResourceGroup',
            fields=[
                ('resourceclassificationgroup', models.CharField(db_column='ResourceClassificationGroup', max_length=255, primary_key=True, serialize=False, verbose_name='broad species group')),
            ],
            options={
                'verbose_name_plural': 'resource groups',
                'db_table': 'LookupResourceGroup',
                'verbose_name': 'resource group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupSeason',
            fields=[
                ('season', models.CharField(db_column='Season', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'seasons',
                'db_table': 'LookupSeason',
                'verbose_name': 'season',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupTechniques',
            fields=[
                ('techniques', models.CharField(db_column='Techniques', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'techniques',
                'db_table': 'LookupTechniques',
                'verbose_name': 'technique',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LookupTiming',
            fields=[
                ('timing', models.CharField(db_column='Timing', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'timings',
                'db_table': 'LookupTiming',
                'verbose_name': 'timing',
                'managed': True,
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
                'verbose_name_plural': 'tribes',
                'db_table': 'LookupTribe',
                'verbose_name': 'tribe',
                'managed': True,
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
                'verbose_name_plural': 'user info',
                'db_table': 'LookupUserInfo',
                'verbose_name': 'user info',
                'managed': True,
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
                'verbose_name_plural': 'people',
                'db_table': 'People',
                'verbose_name': 'person',
                'managed': True,
            },
        ),
    ]
