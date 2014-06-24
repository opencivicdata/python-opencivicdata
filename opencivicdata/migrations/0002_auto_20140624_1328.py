# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='session',
            new_name='legislative_session',
        ),
        migrations.RenameField(
            model_name='relatedbill',
            old_name='session',
            new_name='legislative_session',
        ),
        migrations.RenameField(
            model_name='voteevent',
            old_name='session',
            new_name='legislative_session',
        ),
    ]
