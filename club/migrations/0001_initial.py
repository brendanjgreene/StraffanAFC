# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('mainColor', models.CharField(max_length=255)),
                ('secondColor', models.CharField(max_length=255)),
                ('clubLogo', models.ImageField(null=True, upload_to='images', blank=True)),
                ('backgroundImage', models.ImageField(null=True, upload_to='images', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
    ]
