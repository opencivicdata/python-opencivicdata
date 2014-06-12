# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0016_personvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('vote', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent')),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain'), ('paired', 'Paired')])),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
