# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20170309_1555'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plub',
            new_name='Club',
        ),
    ]