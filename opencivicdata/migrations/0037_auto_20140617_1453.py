# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0036_auto_20140617_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillSponsorship',
            fields=[
                ('id', uuidfield.fields.UUIDField(serialize=False, unique=True, max_length=32, primary_key=True, blank=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id', null=True)),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id', null=True)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BillSponsor',
        ),
    ]
