# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0012_eventparticipant_eventrelatedentity_jurisdictionsession_membership_membershipcontactdetail_membershi'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('post', models.ForeignKey(to_field='id', to='opencivicdata.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
