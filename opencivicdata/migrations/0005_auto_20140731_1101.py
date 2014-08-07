# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0004_auto_20140723_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='division',
            old_name='display_name',
            new_name='name',
        ),
    ]
