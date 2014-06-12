# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import opencivicdata.models.base
import uuidfield.fields
import jsonfield.fields
import djorm_pgarray.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonName',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(max_length=500, blank=True)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='bill', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
                ('subject', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillAction',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('actor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
