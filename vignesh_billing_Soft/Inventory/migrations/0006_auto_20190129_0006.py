# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_auto_20190122_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Products'),
        ),
    ]