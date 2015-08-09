# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import uuid
import opencivicdata.models.base
import django.core.validators
import djorm_pgarray.fields
import django.contrib.gis.db.models.fields
import uuidfield.fields


class Migration(migrations.Migration):

    replaces = [('opencivicdata', '0001_initial'), ('opencivicdata', '0002_auto_20150131_1021'), ('opencivicdata', '0003_auto_20150507_1554'), ('opencivicdata', '0004_auto_20150610_1600'), ('opencivicdata', '0005_auto_20150622_1455'), ('opencivicdata', '0006_auto_20150715_1552')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='bill', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('subject', djorm_pgarray.fields.ArrayField(dbtype='text')),
            ],
        ),
        migrations.CreateModel(
            name='BillAbstract',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('abstract', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='abstracts')),
                ('date', models.TextField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillAction',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('order', models.PositiveIntegerField()),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('action', models.ForeignKey(to='opencivicdata.BillAction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(to='opencivicdata.BillDocument', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='other_identifiers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='sources')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillSponsorship',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('title', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='other_titles')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillVersion',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('version', models.ForeignKey(to='opencivicdata.BillVersion', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=300, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=2)),
                ('subtype1', models.CharField(blank=True, max_length=50)),
                ('subid1', models.CharField(blank=True, max_length=100)),
                ('subtype2', models.CharField(blank=True, max_length=50)),
                ('subid2', models.CharField(blank=True, max_length=100)),
                ('subtype3', models.CharField(blank=True, max_length=50)),
                ('subid3', models.CharField(blank=True, max_length=100)),
                ('subtype4', models.CharField(blank=True, max_length=50)),
                ('subid4', models.CharField(blank=True, max_length=100)),
                ('subtype5', models.CharField(blank=True, max_length=50)),
                ('subid5', models.CharField(blank=True, max_length=100)),
                ('subtype6', models.CharField(blank=True, max_length=50)),
                ('subid6', models.CharField(blank=True, max_length=100)),
                ('subtype7', models.CharField(blank=True, max_length=50)),
                ('subid7', models.CharField(blank=True, max_length=100)),
                ('redirect', models.ForeignKey(null=True, to='opencivicdata.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='event', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('timezone', models.CharField(max_length=300)),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('description', models.TextField()),
                ('order', models.CharField(blank=True, max_length=100)),
                ('subjects', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('notes', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('media', models.ForeignKey(to='opencivicdata.EventAgendaMedia', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDocumentLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(to='opencivicdata.EventDocument', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(to='opencivicdata.Event', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, max_length=2000)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, to='opencivicdata.EventLocation'),
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('media', models.ForeignKey(to='opencivicdata.EventMedia', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(to='opencivicdata.Event', related_name='sources')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='jurisdiction', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$')], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('classification', models.CharField(choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')], default='government', db_index=True, max_length=50)),
                ('feature_flags', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('division', models.ForeignKey(to='opencivicdata.Division')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='event_locations'),
        ),
        migrations.AddField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction'),
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together=set([('jurisdiction', 'start_time', 'name')]),
        ),
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('identifier', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('primary', 'Primary'), ('special', 'Special')], max_length=100)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession'),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='membership', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('membership', models.ForeignKey(to='opencivicdata.Membership', related_name='contact_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MembershipLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('membership', models.ForeignKey(to='opencivicdata.Membership', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='organization', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('classification', models.CharField(choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], blank=True, max_length=100)),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
                ('jurisdiction', models.ForeignKey(null=True, to='opencivicdata.Jurisdiction')),
                ('parent', models.ForeignKey(null=True, to='opencivicdata.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='actions'),
        ),
        migrations.AddField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
        ),
        migrations.AlterIndexTogether(
            name='bill',
            index_together=set([('from_organization', 'legislative_session', 'identifier')]),
        ),
        migrations.AlterIndexTogether(
            name='organization',
            index_together=set([('jurisdiction', 'classification', 'name'), ('classification', 'name')]),
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='contact_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='identifiers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='other_names')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='sources')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='person', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('sort_name', models.CharField(default='', max_length=100)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('gender', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('national_identity', models.CharField(max_length=300)),
                ('biography', models.TextField()),
                ('birth_date', models.CharField(blank=True, max_length=10)),
                ('death_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('person', models.ForeignKey(to='opencivicdata.Person', related_name='contact_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('person', models.ForeignKey(to='opencivicdata.Person', related_name='identifiers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('person', models.ForeignKey(to='opencivicdata.Person', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('person', models.ForeignKey(to='opencivicdata.Person', related_name='other_names')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('person', models.ForeignKey(to='opencivicdata.Person', related_name='sources')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonVote',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')], max_length=50)),
                ('voter_name', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
                ('voter', models.ForeignKey(null=True, to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='post', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('division', models.ForeignKey(null=True, to='opencivicdata.Division', default=None)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, to='opencivicdata.Post'),
        ),
        migrations.AlterIndexTogether(
            name='membership',
            index_together=set([('organization', 'person', 'label', 'post')]),
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([('organization', 'label')]),
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('post', models.ForeignKey(to='opencivicdata.Post', related_name='contact_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('post', models.ForeignKey(to='opencivicdata.Post', related_name='links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RelatedBill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('legislative_session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')], max_length=100)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='related_bills')),
                ('related_bill', models.ForeignKey(null=True, to='opencivicdata.Bill', related_name='related_bills_reverse')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, serialize=False, unique=True, editable=False, max_length=32)),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')], max_length=50)),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoteEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='vote', validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion_text', models.TextField()),
                ('motion_classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('start_date', models.CharField(max_length=19)),
                ('end_date', models.CharField(blank=True, max_length=19)),
                ('result', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=50)),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill')),
                ('legislative_session', models.ForeignKey(to='opencivicdata.LegislativeSession')),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='counts'),
        ),
        migrations.AddField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='votes'),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='vote',
            field=models.ForeignKey(null=True, to='opencivicdata.VoteEvent'),
        ),
        migrations.AlterIndexTogether(
            name='voteevent',
            index_together=set([('legislative_session', 'identifier', 'bill'), ('legislative_session', 'bill')]),
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('vote_event', models.ForeignKey(to='opencivicdata.VoteEvent', related_name='sources')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='family_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='given_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='votecount',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization', related_name='bills'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='bills'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='actions'),
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='action',
            field=models.ForeignKey(to='opencivicdata.BillAction', related_name='related_entities'),
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='documents'),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='sponsorships'),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='versions'),
        ),
        migrations.AlterField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='events'),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='agenda'),
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='agenda_item',
            field=models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='media'),
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='documents'),
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='media'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='participants'),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='agenda_item',
            field=models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='related_entities'),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='division',
            field=models.ForeignKey(to='opencivicdata.Division', related_name='jurisdictions'),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='classification',
            field=models.CharField(choices=[('primary', 'Primary'), ('special', 'Special')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='legislative_sessions'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization', related_name='memberships_on_behalf_of'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, to='opencivicdata.Post', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='jurisdiction',
            field=models.ForeignKey(null=True, to='opencivicdata.Jurisdiction', related_name='organizations'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization', related_name='children'),
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='national_identity',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(null=True, to='opencivicdata.Person', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='post',
            name='division',
            field=models.ForeignKey(null=True, to='opencivicdata.Division', default=None, related_name='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='bill',
            field=models.ForeignKey(null=True, to='opencivicdata.Bill', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='votes'),
        ),
        migrations.AddField(
            model_name='bill',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='event',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='membership',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='organization',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='person',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='post',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
        migrations.AddField(
            model_name='voteevent',
            name='locked_fields',
            field=djorm_pgarray.fields.ArrayField(dbtype='text', default=[]),
        ),
    ]
