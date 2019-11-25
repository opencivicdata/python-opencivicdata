#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BallotMeasureContest-related models.
"""
from django.db import models
from opencivicdata.core.models.base import IdentifierBase, LinkBase
from opencivicdata.core.models import Membership
from .base import ContestBase


class BallotMeasureContest(ContestBase):
    """
    A contest in which voters select from among options proposed in a ballot measure.
    """

    description = models.TextField(
        help_text="Text describing the purpose and/or potential outcomes of the "
        "ballot measure, not necessarily as it appears on the ballot."
    )
    requirement = models.CharField(
        max_length=300,
        blank=True,
        default="50% plus one vote",
        help_text="The threshold of votes the ballot measure needs in order to pass.",
    )
    classification = models.CharField(
        max_length=300,
        blank=True,
        help_text="Describes the origin and/or potential outcome of the ballot "
        'measure, e.g., "initiative statute", "legislative constitutional '
        'amendment".',
    )
    runoff_for_contest = models.OneToOneField(
        "self",
        related_name="runoff_contest",
        null=True,
        on_delete=models.SET_NULL,
        help_text="If this contest is a runoff to determine the outcome of a "
        "previously undecided contest, reference to that "
        "BallotMeasureContest.",
    )

    class Meta(ContestBase.Meta):
        db_table = "opencivicdata_ballotmeasurecontest"


class BallotMeasureContestOption(models.Model):
    """
    An option voters may choose in a BallotMeasureContest.
    """

    contest = models.ForeignKey(
        BallotMeasureContest,
        related_name="options",
        on_delete=models.CASCADE,
        help_text="Reference to the BallotMeasureContest.",
    )
    text = models.CharField(
        max_length=300,
        help_text="Text of the option, not necessarily as it appears on the ballot.",
    )

    def __str__(self):
        return "{0} on {1}".format(self.text, self.contest)

    class Meta:
        db_table = "opencivicdata_ballotmeasurecontestoption"


class BallotMeasureContestIdentifier(IdentifierBase):
    """
    Upstream identifiers of a BallotMeasureContest.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """

    contest = models.ForeignKey(
        BallotMeasureContest,
        related_name="identifiers",
        on_delete=models.CASCADE,
        help_text="Reference to the BallotMeasureContest linked to the upstream "
        "identifier.",
    )

    def __str__(self):
        tmpl = "%s identifies %s"
        return tmpl % (self.identifier, self.contest)

    class Meta:
        db_table = "opencivicdata_ballotmeasurecontestidentifier"


class BallotMeasureContestSource(LinkBase):
    """
    Source used in assembling a BallotMeasureContest.
    """

    contest = models.ForeignKey(
        BallotMeasureContest,
        related_name="sources",
        on_delete=models.CASCADE,
        help_text="Reference to the BallotMeasureContest assembled from the source.",
    )

    class Meta:
        db_table = "opencivicdata_ballotmeasurecontestsource"


class RetentionContest(ContestBase):
    """
    A contest where voters vote to retain or recall a current office holder.

    These contests include judicial retention or recall elections.
    """

    description = models.TextField(
        help_text="Text describing the purpose and/or potential outcomes of the "
        "contest, not necessarily as it appears on the ballot."
    )
    requirement = models.CharField(
        max_length=300,
        blank=True,
        default="50% plus one vote",
        help_text="The threshold of votes need in order to retain the officeholder.",
    )
    runoff_for_contest = models.OneToOneField(
        "self",
        related_name="runoff_contest",
        null=True,
        on_delete=models.SET_NULL,
        help_text="If this contest is a runoff to determine the outcome of a previously "
        "undecided contest, reference to that RetentionContest.",
    )
    membership = models.ForeignKey(
        Membership,
        help_text="Reference to the Membership that represents the tenure of a "
        "person in a specific public office.",
        on_delete=models.PROTECT,
    )

    class Meta(ContestBase.Meta):
        db_table = "opencivicdata_retentioncontest"


class RetentionContestOption(models.Model):
    """
    An option voters may choose in a RetentionContest.
    """

    contest = models.ForeignKey(
        RetentionContest,
        related_name="options",
        help_text="Reference to the RetentionContest.",
        on_delete=models.CASCADE,
    )
    text = models.CharField(
        max_length=300,
        help_text="Text of the option, not necessarily as it appears on the ballot.",
    )

    def __str__(self):
        return "{0} on {1}".format(self.text, self.contest)

    class Meta:
        db_table = "opencivicdata_retentioncontestoption"


class RetentionContestIdentifier(IdentifierBase):
    """
    Upstream identifiers of a RetentionContest.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """

    contest = models.ForeignKey(
        RetentionContest,
        related_name="identifiers",
        help_text="Reference to the RetentionContest linked to the upstream "
        "identifier.",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        tmpl = "%s identifies %s"
        return tmpl % (self.identifier, self.contest)

    class Meta:
        db_table = "opencivicdata_retentionidentifier"


class RetentionContestSource(LinkBase):
    """
    Source used in assembling a RetentionContest.
    """

    contest = models.ForeignKey(
        RetentionContest,
        related_name="sources",
        help_text="Reference to the RetentionContest assembled from the source.",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "opencivicdata_retentionsource"
