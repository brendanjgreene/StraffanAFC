# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='homefield',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='lat',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='long',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
    ]
