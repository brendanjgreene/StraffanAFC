# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_stafftitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='stafftitle',
            name='is_staff',
            field=models.BooleanField(default=False, help_text=b'Designates whether the user can log into this admin site.'),
        ),
        migrations.AddField(
            model_name='stafftitle',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text=b'Designates whether the user can log into all admin site.'),
        ),
    ]
