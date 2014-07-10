# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0003_auto_20140709_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventagendaitem',
            name='event',
            field=models.ForeignKey(default=None, to='opencivicdata.Event'),
            preserve_default=False,
        ),
    ]
