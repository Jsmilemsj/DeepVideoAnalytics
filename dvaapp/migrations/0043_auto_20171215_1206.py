# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-15 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0042_delete_vdnserver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeddvapql',
            name='creator',
        ),
        migrations.DeleteModel(
            name='StoredDVAPQL',
        ),
    ]