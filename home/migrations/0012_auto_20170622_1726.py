# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170610_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stafftitle',
            name='is_staff',
            field=models.BooleanField(default=True, help_text=b'Designates whether the user can log into this admin site.'),
        ),
    ]
