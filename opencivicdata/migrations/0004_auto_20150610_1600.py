# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0003_auto_20150507_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billabstract',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billdocumentlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billidentifier',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billsource',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='billversionlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventagendamedialink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventdocumentlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventmedialink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='membershipcontactdetail',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='membershiplink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='organizationcontactdetail',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='organizationidentifier',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='organizationlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='organizationsource',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='personcontactdetail',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='personidentifier',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='personlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='personname',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='personsource',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='postcontactdetail',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='postlink',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='votecount',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='votesource',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False),
        ),
    ]
