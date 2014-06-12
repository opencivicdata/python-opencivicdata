# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import opencivicdata.models.base
import uuidfield.fields
import jsonfield.fields
import django.core.validators
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='person', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('gender', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('national_identity', models.CharField(max_length=300)),
                ('biography', models.TextField()),
                ('birth_date', models.CharField(max_length=10, blank=True)),
                ('death_date', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('description', models.TextField()),
                ('order', models.CharField(max_length=100, blank=True)),
                ('subjects', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaItem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
