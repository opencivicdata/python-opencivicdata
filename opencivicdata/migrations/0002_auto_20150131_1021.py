# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='family_name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='given_name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
    ]
