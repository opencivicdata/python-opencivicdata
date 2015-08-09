# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_squashed_0006_auto_20150715_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='classification',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='bill',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='bill',
            name='subject',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='classification',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='event',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='notes',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='subjects',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='feature_flags',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='membership',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='organization',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='person',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='post',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='locked_fields',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='motion_classification',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.TextField(), default=list),
        ),
    ]
