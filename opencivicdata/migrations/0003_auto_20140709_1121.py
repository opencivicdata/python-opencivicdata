# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_auto_20140708_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='chamber',
        ),
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], max_length=100, blank=True),
        ),
    ]
