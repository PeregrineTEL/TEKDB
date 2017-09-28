# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 01:12
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('accessid', models.AutoField(db_column='AccessID', primary_key=True, serialize=False)),
                ('accesslevel', models.CharField(blank=True, db_column='AccessLevel', max_length=255, null=True, verbose_name='access level')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'user access',
                'managed': True,
                'verbose_name': 'user access',
                'db_table': 'UserAccess',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='UserName', max_length=20, unique=True, verbose_name='username')),
                ('password', models.CharField(db_column='Password', max_length=128, verbose_name='password')),
                ('first_name', models.CharField(db_column='FirstName', max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(db_column='LastName', max_length=255, verbose_name='last name')),
                ('affiliation', models.CharField(db_column='Affiliation', max_length=255)),
                ('title', models.CharField(db_column='Title', max_length=255)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('accesslevel', models.ForeignKey(blank=True, db_column='AccessLevel', null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.UserAccess', verbose_name='access level')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'managed': True,
                'verbose_name': 'User',
                'db_table': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
