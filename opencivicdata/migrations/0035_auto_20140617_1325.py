# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0034_auto_20140616_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdocument',
            old_name='mimetype',
            new_name='media_type',
        ),
        migrations.RenameField(
            model_name='billdocumentlink',
            old_name='mimetype',
            new_name='media_type',
        ),
        migrations.RenameField(
            model_name='eventagendamedialink',
            old_name='mimetype',
            new_name='media_type',
        ),
        migrations.RenameField(
            model_name='eventmedialink',
            old_name='mimetype',
            new_name='media_type',
        ),
        migrations.RenameField(
            model_name='billversionlink',
            old_name='mimetype',
            new_name='media_type',
        ),
    ]
