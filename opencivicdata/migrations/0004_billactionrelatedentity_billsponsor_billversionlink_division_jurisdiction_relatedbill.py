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
        ('opencivicdata', '0003_billdocumentlink_billname_billsource_billsummary_billtitle_billversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to_field='id', to='opencivicdata.BillVersion')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedBill',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('related_bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill', null=True)),
                ('name', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(max_length=100, choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('action', models.ForeignKey(to_field='id', to='opencivicdata.BillAction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSponsor',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=300, serialize=False)),
                ('display_name', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=2)),
                ('subtype1', models.CharField(max_length=50, blank=True)),
                ('subid1', models.CharField(max_length=100, blank=True)),
                ('subtype2', models.CharField(max_length=50, blank=True)),
                ('subid2', models.CharField(max_length=100, blank=True)),
                ('subtype3', models.CharField(max_length=50, blank=True)),
                ('subid3', models.CharField(max_length=100, blank=True)),
                ('subtype4', models.CharField(max_length=50, blank=True)),
                ('subid4', models.CharField(max_length=100, blank=True)),
                ('subtype5', models.CharField(max_length=50, blank=True)),
                ('subid5', models.CharField(max_length=100, blank=True)),
                ('subtype6', models.CharField(max_length=50, blank=True)),
                ('subid6', models.CharField(max_length=100, blank=True)),
                ('subtype7', models.CharField(max_length=50, blank=True)),
                ('subid7', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='jurisdiction', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', flags=32)], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('classification', models.CharField(default='government', max_length=50, choices=[('government', 'Government'), ('school board', 'School Board')])),
                ('feature_flags', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
                ('division', models.ForeignKey(to_field='id', to='opencivicdata.Division')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
