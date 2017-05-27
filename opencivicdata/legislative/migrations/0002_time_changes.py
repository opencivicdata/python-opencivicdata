# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voteevent',
            old_name='end_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='voteevent',
            old_name='start_date',
            new_name='start_time',
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='end_time',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='start_time',
            field=models.CharField(max_length=25),
        ),
        migrations.RenameField(
            model_name='billaction',
            old_name='date',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='billaction',
            name='time',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.CharField(blank=True, default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(max_length=25),
        ),
    ]
