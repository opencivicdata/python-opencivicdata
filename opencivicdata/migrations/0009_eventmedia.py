# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0008_eventlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
