# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-11 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Address', models.TextField()),
                ('Mobile', models.IntegerField()),
                ('GST', models.CharField(max_length=30)),
                ('DL_No', models.CharField(max_length=30)),
                ('Outstanding', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Free', models.IntegerField()),
                ('GST', models.FloatField(blank=True, default=None, null=True)),
                ('Qty', models.IntegerField()),
                ('Discount', models.FloatField(blank=True, default=None, null=True)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Customers')),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='p_id',
        ),
        migrations.AlterField(
            model_name='products',
            name='Exp_Date',
            field=models.DateField(verbose_name='Expiry Date'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Products'),
        ),
    ]
