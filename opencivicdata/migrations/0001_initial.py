# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import opencivicdata.models.base
import django.core.validators
import uuid
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='bill', serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('subject', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
            ],
        ),
        migrations.CreateModel(
            name='BillAbstract',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('abstract', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('date', models.TextField(blank=True, max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='abstracts')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillAction',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('order', models.PositiveIntegerField()),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='actions')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('action', models.ForeignKey(to='opencivicdata.BillAction', related_name='related_entities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='documents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='sponsorships')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='versions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.CharField(primary_key=True, serialize=False, max_length=300)),
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
                ('redirect', models.ForeignKey(to='opencivicdata.Division', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='event', serialize=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('description', models.TextField()),
                ('order', models.CharField(blank=True, max_length=100)),
                ('subjects', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('notes', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('event', models.ForeignKey(to='opencivicdata.Event', related_name='agenda')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='media')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('event', models.ForeignKey(to='opencivicdata.Event', related_name='documents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDocumentLink',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, max_length=2000)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(to='opencivicdata.Event', related_name='media')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('event', models.ForeignKey(to='opencivicdata.Event', related_name='participants')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='related_entities')),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', flags=32)], ocd_type='jurisdiction', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('classification', models.CharField(db_index=True, choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')], max_length=50, default='government')),
                ('feature_flags', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('division', models.ForeignKey(to='opencivicdata.Division', related_name='jurisdictions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('identifier', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(blank=True, max_length=100, choices=[('primary', 'Primary'), ('special', 'Special')])),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='legislative_sessions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='membership', serialize=False)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='organization', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('classification', models.CharField(blank=True, max_length=100, choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')])),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='organizations', null=True)),
                ('parent', models.ForeignKey(to='opencivicdata.Organization', related_name='children', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='person', serialize=False)),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('sort_name', models.CharField(default='', max_length=100)),
                ('family_name', models.CharField(blank=True, max_length=100)),
                ('given_name', models.CharField(blank=True, max_length=100)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('summary', models.CharField(blank=True, max_length=500)),
                ('national_identity', models.CharField(blank=True, max_length=300)),
                ('biography', models.TextField(blank=True)),
                ('birth_date', models.CharField(blank=True, max_length=10)),
                ('death_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')], max_length=50)),
                ('voter_name', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='post', serialize=False)),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('division', models.ForeignKey(to='opencivicdata.Division', default=None, related_name='posts', null=True)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='posts')),
            ],
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('identifier', models.CharField(max_length=100)),
                ('legislative_session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')], max_length=100)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='related_bills')),
                ('related_bill', models.ForeignKey(to='opencivicdata.Bill', related_name='related_bills_reverse', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='vote', serialize=False)),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion_text', models.TextField()),
                ('motion_classification', django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.TextField(), default=list)),
                ('start_date', models.CharField(max_length=19)),
                ('end_date', models.CharField(blank=True, max_length=19)),
                ('result', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=50)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', related_name='votes', null=True)),
                ('legislative_session', models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='votes')),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', related_name='votes')),
            ],
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('vote_event', models.ForeignKey(to='opencivicdata.VoteEvent', related_name='sources')),
            ],
            options={
                'abstract': False,
            },
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
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='votes', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='memberships_on_behalf_of', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='memberships'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='memberships'),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(to='opencivicdata.Post', related_name='memberships', null=True),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
        ),
        migrations.AddField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='event_locations'),
        ),
        migrations.AddField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='events'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(to='opencivicdata.EventLocation', null=True),
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
        ),
        migrations.AddField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='actions'),
        ),
        migrations.AddField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='bills', null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='bills'),
        ),
        migrations.AlterIndexTogether(
            name='voteevent',
            index_together=set([('legislative_session', 'identifier', 'bill'), ('legislative_session', 'bill')]),
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([('organization', 'label')]),
        ),
        migrations.AlterIndexTogether(
            name='organization',
            index_together=set([('jurisdiction', 'classification', 'name'), ('classification', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='membership',
            index_together=set([('organization', 'person', 'label', 'post')]),
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together=set([('jurisdiction', 'start_time', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='bill',
            index_together=set([('from_organization', 'legislative_session', 'identifier')]),
        ),
    ]
