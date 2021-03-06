# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-21 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_auto_20190112_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='Address',
            new_name='Addr',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='DL_No',
            new_name='Lic',
        ),
        migrations.AddField(
            model_name='customers',
            name='Premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Products'),
        ),
    ]
