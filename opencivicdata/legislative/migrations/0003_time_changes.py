# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("legislative", "0002_more_extras")]

    operations = [
        migrations.RunSQL(
            "SET CONSTRAINTS ALL IMMEDIATE", reverse_sql=migrations.RunSQL.noop
        ),
        migrations.AlterField(
            model_name="voteevent",
            name="end_date",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name="voteevent",
            name="start_date",
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name="billaction", name="date", field=models.CharField(max_length=25)
        ),
        migrations.AlterField(
            model_name="event",
            name="end_time",
            field=models.CharField(blank=True, default="", max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="event", name="start_time", field=models.CharField(max_length=25)
        ),
        migrations.RenameField(
            model_name="event", old_name="end_time", new_name="end_date"
        ),
        migrations.RenameField(
            model_name="event", old_name="start_time", new_name="start_date"
        ),
        migrations.AlterIndexTogether(
            name="event", index_together=set([("jurisdiction", "start_date", "name")])
        ),
        migrations.RemoveField(model_name="event", name="timezone"),
        migrations.RunSQL(
            migrations.RunSQL.noop, reverse_sql="SET CONSTRAINTS ALL IMMEDIATE"
        ),
    ]
