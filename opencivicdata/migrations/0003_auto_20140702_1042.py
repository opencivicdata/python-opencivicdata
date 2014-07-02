# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_auto_20140624_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='entity_type',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='entity_type',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='entity_type',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='entity_type',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
