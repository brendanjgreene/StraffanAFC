# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20170629_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(related_name='staff_name', blank=True, to='home.Team', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.ForeignKey(related_name='staff_name', blank=True, to='home.StaffTitle', null=True),
        ),
    ]
