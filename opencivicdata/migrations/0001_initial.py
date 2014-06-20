# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields
import opencivicdata.models.base
import djorm_pgarray.fields
import django.core.validators
import jsonfield.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='bill', serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('subject', djorm_pgarray.fields.ArrayField(dbtype='text')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillAbstract',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('abstract', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillAction',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('order', models.PositiveIntegerField()),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('action', models.ForeignKey(to_field='id', to='opencivicdata.BillAction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to_field='id', to='opencivicdata.BillDocument')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
            name='BillSponsorship',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('title', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersion',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to_field='id', to='opencivicdata.BillVersion')),
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
                ('redirect', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Division')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='event', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20, choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('description', models.TextField()),
                ('order', models.CharField(max_length=100, blank=True)),
                ('subjects', djorm_pgarray.fields.ArrayField(dbtype='text')),
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
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaItem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=300)),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.EventLocation'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to_field='id', to='opencivicdata.EventMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('note', models.TextField()),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('note', models.TextField()),
                ('agenda_item', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', flags=32, message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$')], ocd_type='jurisdiction', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('classification', models.CharField(default='government', max_length=50, choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')])),
                ('feature_flags', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('division', models.ForeignKey(to_field='id', to='opencivicdata.Division')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='JurisdictionSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(max_length=100, choices=[('primary', 'Primary'), ('special', 'Special')])),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bill',
            name='session',
            field=models.ForeignKey(to_field='id', to='opencivicdata.JurisdictionSession'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='membership', serialize=False)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('role', models.CharField(max_length=300, blank=True)),
                ('start_date', models.CharField(max_length=10, blank=True)),
                ('end_date', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('membership', models.ForeignKey(to_field='id', to='opencivicdata.Membership')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('membership', models.ForeignKey(to_field='id', to='opencivicdata.Membership')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='organization', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('classification', models.CharField(max_length=100, choices=[('legislature', 'Legislature'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], blank=True)),
                ('chamber', models.CharField(max_length=10, blank=True)),
                ('founding_date', models.CharField(max_length=10, blank=True)),
                ('dissolution_date', models.CharField(max_length=10, blank=True)),
                ('jurisdiction', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Jurisdiction')),
                ('parent', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='organization',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='organization',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationName',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(max_length=500, blank=True)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='person', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('sort_name', models.CharField(default='', max_length=100)),
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
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='person',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='person',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
            name='PersonVote',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired')])),
                ('voter_name', models.CharField(max_length=300)),
                ('voter', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='post', serialize=False)),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=300, blank=True)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('division', models.ForeignKey(default=None, null=True, to_field='id', to='opencivicdata.Division')),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.Post'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
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
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('post', models.ForeignKey(to_field='id', to='opencivicdata.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedBill',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(max_length=100, choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')])),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('related_bill', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired')])),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='vote', serialize=False)),
                ('identifier', models.CharField(max_length=300, blank=True)),
                ('motion_text', models.TextField()),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10, blank=True)),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('result', models.CharField(max_length=50, choices=[('pass', 'Pass'), ('fail', 'Fail')])),
                ('bill', models.ForeignKey(null=True, to_field='id', to='opencivicdata.Bill')),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
                ('session', models.ForeignKey(to_field='id', to='opencivicdata.JurisdictionSession')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='vote',
            field=models.ForeignKey(null=True, to_field='id', to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, blank=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('vote_event', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
