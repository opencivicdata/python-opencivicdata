# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0004_auto_20150925_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventagendaitem',
            name='classification',
            field=ArrayField(base_field=models.TextField(), blank=True, default=list, size=None),
        ),
    ]

