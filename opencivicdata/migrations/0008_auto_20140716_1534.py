# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0007_event_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdocumentlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='billsource',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='billversionlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventagendamedialink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventdocumentlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='eventmedialink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='membershiplink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='organization',
            name='image',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='organizationlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='organizationsource',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='personlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='personsource',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='postlink',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='votesource',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
