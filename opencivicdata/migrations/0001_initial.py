# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import opencivicdata.models.base
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='bill', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('identifier', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('subject', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='BillAbstract',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('abstract', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('date', models.TextField(blank=True, max_length=10)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstracts', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillAction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('order', models.PositiveIntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='opencivicdata.Bill')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_entities', to='opencivicdata.BillAction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.BillDocument')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_identifiers', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillSponsorship',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorships', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_titles', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.BillVersion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
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
                ('redirect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='event', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('order', models.CharField(blank=True, max_length=100)),
                ('subjects', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('notes', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='opencivicdata.EventAgendaItem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.EventAgendaMedia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDocumentLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.EventDocument')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, max_length=2000)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.EventMedia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('agenda_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_entities', to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='opencivicdata.Event')),
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
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='jurisdiction', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$')])),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('classification', models.CharField(choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')], db_index=True, default='government', max_length=50)),
                ('feature_flags', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurisdictions', to='opencivicdata.Division')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(blank=True, choices=[('primary', 'Primary'), ('special', 'Special')], max_length=100)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('jurisdiction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legislative_sessions', to='opencivicdata.Jurisdiction')),
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
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='membership', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('label', models.CharField(blank=True, max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_details', to='opencivicdata.Membership')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MembershipLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.Membership')),
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
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='organization', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('classification', models.CharField(blank=True, choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], max_length=100)),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
                ('jurisdiction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='opencivicdata.Jurisdiction')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='opencivicdata.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_details', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_names', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='opencivicdata.Organization')),
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
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='person', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_details', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_names', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonVote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
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
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='post', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('division', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='opencivicdata.Division')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='opencivicdata.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_details', to='opencivicdata.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='opencivicdata.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RelatedBill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('legislative_session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')], max_length=100)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_bills', to='opencivicdata.Bill')),
                ('related_bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_bills_reverse', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
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
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='vote', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion_text', models.TextField()),
                ('motion_classification', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('start_date', models.CharField(max_length=19)),
                ('end_date', models.CharField(blank=True, max_length=19)),
                ('result', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=50)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='opencivicdata.Bill')),
                ('legislative_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='opencivicdata.LegislativeSession')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='opencivicdata.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('vote_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='opencivicdata.VoteEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counts', to='opencivicdata.VoteEvent'),
        ),
        migrations.AddField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='opencivicdata.VoteEvent'),
        ),
        migrations.AddField(
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships_on_behalf_of', to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='opencivicdata.Post'),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='vote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.VoteEvent'),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_locations', to='opencivicdata.Jurisdiction'),
        ),
        migrations.AddField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='opencivicdata.Jurisdiction'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.EventLocation'),
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opencivicdata.Person'),
        ),
        migrations.AddField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='opencivicdata.Organization'),
        ),
        migrations.AddField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='opencivicdata.LegislativeSession'),
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
            index_together=set([('classification', 'name'), ('jurisdiction', 'classification', 'name')]),
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
