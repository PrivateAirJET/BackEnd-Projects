# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Jet Tamani', max_length=120),
            preserve_default=False,
        ),
    ]
