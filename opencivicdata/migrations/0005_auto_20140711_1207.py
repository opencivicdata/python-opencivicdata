# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0004_eventagendaitem_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdocument',
            old_name='name',
            new_name='note',
        ),
    ]
