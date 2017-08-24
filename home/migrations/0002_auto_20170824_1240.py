# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='mobile',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
