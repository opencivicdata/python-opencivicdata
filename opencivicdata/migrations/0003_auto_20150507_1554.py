# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_auto_20150131_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='billabstract',
            name='date',
            field=models.TextField(blank=True, max_length=10),
            preserve_default=True,
        ),
    ]
