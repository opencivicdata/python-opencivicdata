# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0037_auto_20140617_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relatedbill',
            old_name='name',
            new_name='identifier',
        ),
    ]
