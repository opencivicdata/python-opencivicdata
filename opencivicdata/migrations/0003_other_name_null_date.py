# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_auto_20150131_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationname',
            name='end_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='start_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personname',
            name='end_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personname',
            name='start_date',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
