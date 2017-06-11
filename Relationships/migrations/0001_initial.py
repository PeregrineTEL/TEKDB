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
            name='LocalityGISSelections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localitylabel', models.CharField(blank=True, db_column='LocalityLabel', max_length=255, null=True, verbose_name='locality label')),
                ('sourcefc', models.CharField(blank=True, db_column='SourceFC', max_length=255, null=True, verbose_name='source fc')),
            ],
            options={
                'verbose_name_plural': 'Locality GIS Selections',
                'db_table': 'LocalityGISSelections',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LocalityPlaceResourceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
            ],
            options={
                'verbose_name_plural': 'Localities - Place-Resources',
                'db_table': 'LocalityPlaceResourceEvent',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MediaCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Media - Citations',
                'managed': True,
                'verbose_name': 'Medium - Citation',
                'db_table': 'MediaCitationEvents',
            },
        ),
        migrations.CreateModel(
            name='PlaceAltIndigenousName',
            fields=[
                ('altindigenousnameid', models.AutoField(db_column='AltIndigenousNameID', primary_key=True, serialize=False)),
                ('altindigenousname', models.CharField(blank=True, db_column='AltIndigenousName', max_length=255, null=True, verbose_name='alternate indigenous name')),
            ],
            options={
                'verbose_name_plural': 'Places - Indigenous Names',
                'db_table': 'PlaceAltIndigenousName',
                'verbose_name': 'Place - Indigenous Name',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlaceGISSelections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placelabel', models.CharField(blank=True, db_column='PlaceLabel', max_length=255, null=True, verbose_name='label')),
                ('sourcefc', models.CharField(blank=True, db_column='SourceFC', max_length=255, null=True, verbose_name='source fc')),
            ],
            options={
                'verbose_name_plural': 'Place GIS Selections',
                'db_table': 'PlaceGISSelections',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlacesCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Places - Citations',
                'managed': True,
                'verbose_name': 'Place - Citation',
                'db_table': 'PlacesCitationEvents',
            },
        ),
        migrations.CreateModel(
            name='PlacesMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Places - Media',
                'managed': True,
                'verbose_name': 'Place - Medium',
                'db_table': 'PlacesMediaEvents',
            },
        ),
        migrations.CreateModel(
            name='PlacesResourceCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Place-Resources - Citations',
                'db_table': 'PlacesResourceCitationEvents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlacesResourceEvents',
            fields=[
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('placeresourceid', models.AutoField(db_column='PlaceResourceID', primary_key=True, serialize=False)),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('barterresource', models.BooleanField(db_column='BarterResource', default=False, verbose_name='barter resource?')),
                ('january', models.BooleanField(db_column='January', default=False)),
                ('february', models.BooleanField(db_column='February', default=False)),
                ('march', models.BooleanField(db_column='March', default=False)),
                ('april', models.BooleanField(db_column='April', default=False)),
                ('may', models.BooleanField(db_column='May', default=False)),
                ('june', models.BooleanField(db_column='June', default=False)),
                ('july', models.BooleanField(db_column='July', default=False)),
                ('august', models.BooleanField(db_column='August', default=False)),
                ('september', models.BooleanField(db_column='September', default=False)),
                ('october', models.BooleanField(db_column='October', default=False)),
                ('november', models.BooleanField(db_column='November', default=False)),
                ('december', models.BooleanField(db_column='December', default=False)),
                ('year', models.IntegerField(blank=True, db_column='Year', null=True)),
                ('islocked', models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')),
            ],
            options={
                'verbose_name_plural': 'Places - Resources',
                'db_table': 'PlacesResourceEvents',
                'verbose_name': 'Place - Resource',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlacesResourceMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Place-Resources - Media',
                'db_table': 'PlacesResourceMediaEvents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResourceActivityCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Activity - Citations',
                'db_table': 'ResourceActivityCitationEvents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResourceActivityMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Activity - Media',
                'db_table': 'ResourceActivityMediaEvents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResourceAltIndigenousName',
            fields=[
                ('altindigenousnameid', models.AutoField(db_column='AltIndigenousNameID', primary_key=True, serialize=False)),
                ('altindigenousname', models.CharField(blank=True, db_column='AltIndigenousName', max_length=255, null=True, verbose_name='alt indigenous name')),
            ],
            options={
                'verbose_name_plural': 'Resource Alternative Indigenous Names',
                'db_table': 'ResourceAltIndigenousName',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResourceResourceEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
            ],
            options={
                'verbose_name_plural': 'Resources - Resources',
                'db_table': 'ResourceResourceEvents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResourcesCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Resources - Citations',
                'managed': True,
                'verbose_name': 'Resource - Citation',
                'db_table': 'ResourcesCitationEvents',
            },
        ),
        migrations.CreateModel(
            name='ResourcesMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='EnteredByName', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='EnteredByTribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='EnteredByTitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='EnteredByDate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='ModifiedByName', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='ModifiedByTitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='ModifiedByTribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='ModifiedByDate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='RelationshipDescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='Pages', max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Resources - Media',
                'managed': True,
                'verbose_name': 'Resource - Medium',
                'db_table': 'ResourcesMediaEvents',
            },
        ),
    ]
