# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-04-30 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeno', '0004_zenoitem_client_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zenoitem',
            old_name='client_url',
            new_name='url',
        ),
    ]