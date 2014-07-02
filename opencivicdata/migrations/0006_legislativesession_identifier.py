# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0005_auto_20140702_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislativesession',
            name='identifier',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
