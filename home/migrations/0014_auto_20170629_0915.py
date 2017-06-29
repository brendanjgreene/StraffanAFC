# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0013_auto_20170626_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=20, blank=True)),
                ('team', models.ForeignKey(related_name='staff_name', blank=True, to='home.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='stafftitle',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='stafftitle',
            name='is_superuser',
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.ForeignKey(related_name='staff_name', blank=True, to='home.StaffTitle'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
