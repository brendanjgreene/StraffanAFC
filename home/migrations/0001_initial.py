# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=20)),
                ('parent_name', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=20, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to='images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ['age'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(related_name='staff_name', blank=True, to='home.Team', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.ForeignKey(related_name='staff_name', blank=True, to='home.StaffTitle', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name='player_name', to='home.Team'),
        ),
    ]
