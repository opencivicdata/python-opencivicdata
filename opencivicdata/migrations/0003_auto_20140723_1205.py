# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_personvote_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationname',
            name='name',
            field=models.CharField(db_index=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='personname',
            name='name',
            field=models.CharField(db_index=True, max_length=500),
        ),
    ]
