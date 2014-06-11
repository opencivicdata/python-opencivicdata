# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import jsonfield.fields
import uuidfield.fields
import djorm_pgarray.fields
import opencivicdata.models.base
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('description', models.TextField()),
                ('order', models.CharField(blank=True, max_length=100)),
                ('subjects', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='person', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('gender', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('national_identity', models.CharField(max_length=300)),
                ('biography', models.TextField()),
                ('birth_date', models.CharField(blank=True, max_length=10)),
                ('death_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=10)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='bill', serialize=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('action', models.ForeignKey(to_field='id', to='opencivicdata.BillAction')),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSponsor',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(serialize=False, max_length=300, primary_key=True)),
                ('display_name', models.CharField(max_length=300)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$')], ocd_type='jurisdiction', serialize=False)),
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
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='event', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction')),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20, choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')])),
                ('location', models.ForeignKey(to_field='id', to='opencivicdata.EventLocation', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=10)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to_field='id', to='opencivicdata.EventMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JurisdictionSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction')),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(max_length=100, choices=[('primary', 'Primary'), ('special', 'Special')])),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
                ('note', models.TextField()),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('agenda_item', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill', null=True)),
                ('note', models.TextField()),
                ('vote', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent', null=True)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='membership', serialize=False)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
                ('label', models.CharField(blank=True, max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='organization', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction', null=True)),
                ('classification', models.CharField(blank=True, max_length=100, choices=[('legislature', 'Legislature'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')])),
                ('chamber', models.CharField(blank=True, max_length=10)),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='post', serialize=False)),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('post', models.ForeignKey(to_field='id', to='opencivicdata.Post')),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], ocd_type='vote', serialize=False)),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion', models.TextField()),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True)),
                ('outcome', models.CharField(max_length=50, choices=[('pass', 'Pass'), ('fail', 'Fail')])),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
                ('session', models.ForeignKey(to_field='id', to='opencivicdata.JurisdictionSession')),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonVote',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('vote', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent')),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain'), ('paired', 'Paired')])),
                ('voter_name', models.CharField(max_length=300)),
                ('voter', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('vote', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent')),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain'), ('paired', 'Paired')])),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, primary_key=True, blank=True, serialize=False, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent')),
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
        migrations.AddField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='division',
            name='redirect',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Division', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Post', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
    ]
