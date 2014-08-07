# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0003_auto_20140723_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billversionlink',
            old_name='document',
            new_name='version',
        ),
    ]
