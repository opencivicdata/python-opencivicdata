# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlocation',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
