# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wotlogin', '0004_petdisease_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='petbirthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='petbreed',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='petname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pettype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='petdisease',
            name='addedkeyword',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='petdisease',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='petdisease',
            name='discription',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='petdisease',
            name='disease',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='petdisease',
            name='potentialkeyword',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='petdisease',
            name='userkeyword',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]