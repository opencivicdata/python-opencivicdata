# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0009_eventmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to_field='id', to='opencivicdata.EventMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
