# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import opencivicdata.models.base
import uuidfield.fields
import jsonfield.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0011_eventsource'),
    ]

    operations = [
        migrations.CreateModel(
            name='JurisdictionSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('event', models.ForeignKey(to_field='id', to='opencivicdata.Event')),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person', null=True)),
                ('agenda_item', models.ForeignKey(to_field='id', to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill', null=True)),
                ('note', models.TextField()),
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
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='membership', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.Person')),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='organization', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction', null=True)),
                ('classification', models.CharField(blank=True, max_length=100, choices=[('legislature', 'Legislature'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')])),
                ('chamber', models.CharField(max_length=10, blank=True)),
                ('founding_date', models.CharField(max_length=10, blank=True)),
                ('dissolution_date', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
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
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='post', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=300, blank=True)),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
