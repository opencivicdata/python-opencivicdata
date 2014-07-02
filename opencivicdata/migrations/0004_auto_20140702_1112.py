# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0003_auto_20140702_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voteevent',
            old_name='classification',
            new_name='motion_classification',
        ),
    ]
