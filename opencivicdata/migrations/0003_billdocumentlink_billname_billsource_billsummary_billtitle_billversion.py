# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_bill_billaction_billdocument_eventagendamedialink_personcontactdetail_personidentifier_personlink_pe'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to_field='id', to='opencivicdata.BillDocument')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillName',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('name', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSummary',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('text', models.TextField()),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('text', models.TextField()),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersion',
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
