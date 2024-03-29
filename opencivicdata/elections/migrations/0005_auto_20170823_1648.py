# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("elections", "0004_field_docs")]

    operations = [
        migrations.AlterField(
            model_name="candidacy",
            name="party",
            field=models.ForeignKey(
                help_text="Reference to the Organization representing the political party that nominated the candidate or would nominate the candidate (as in the case of a partisan primary).", # noqa
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="candidacies",
                to="core.Organization",
            ),
        ),
        migrations.AlterField(
            model_name="candidacy",
            name="post",
            field=models.ForeignKey(
                help_text="Reference to Post representing the public office for which the candidate is seeking election.", # noqa
                on_delete=django.db.models.deletion.CASCADE,
                related_name="candidacies",
                to="core.Post",
            ),
        ),
        migrations.AlterField(
            model_name="candidatecontest",
            name="party",
            field=models.ForeignKey(
                help_text="If the contest is among candidates of the same political party, e.g., a partisan primary election, reference to the Organization representing that party.", # noqa
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="candidate_contests",
                to="core.Organization",
            ),
        ),
        migrations.AlterField(
            model_name="candidatecontestpost",
            name="post",
            field=models.ForeignKey(
                help_text="Reference to the Post representing a public office at stake in the CandidateContest.", # noqa
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contests",
                to="core.Post",
            ),
        ),
        migrations.AlterField(
            model_name="partycontestoption",
            name="contest",
            field=models.ForeignKey(
                help_text="Reference to the PartyContest in which the party is an option.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="parties",
                to="elections.PartyContest",
            ),
        ),
        migrations.AlterField(
            model_name="partycontestoption",
            name="party",
            field=models.ForeignKey(
                help_text="Reference to an Organization representing a political party voters may choose in the contest.", # noqa
                on_delete=django.db.models.deletion.CASCADE,
                related_name="party_contests",
                to="core.Organization",
            ),
        ),
    ]
