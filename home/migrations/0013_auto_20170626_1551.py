# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20170622_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='parent_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
