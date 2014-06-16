# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0033_auto_20140616_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billaction',
            old_name='description',
            new_name='text',
        ),
    ]
