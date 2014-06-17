# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0038_auto_20140617_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventmedia',
            old_name='name',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='eventagendamedia',
            old_name='name',
            new_name='note',
        ),
        migrations.RemoveField(
            model_name='eventmedia',
            name='type',
        ),
        migrations.RemoveField(
            model_name='eventagendamedia',
            name='type',
        ),
    ]
