# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0008_auto_20140716_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='name',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='name',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='name',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='name',
            field=models.CharField(max_length=2000),
        ),
    ]
