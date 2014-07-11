# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0006_auto_20140711_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='timezone',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]
