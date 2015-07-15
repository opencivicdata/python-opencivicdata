# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0005_auto_20150622_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='event',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='membership',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='organization',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='person',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='post',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
        migrations.AddField(
            model_name='voteevent',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(default=[], dbtype='text'),
        ),
    ]
