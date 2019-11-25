#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base classes for contest-related models.
"""
from django.db import models
from opencivicdata.core.models.base import OCDBase, OCDIDField
from opencivicdata.core.models import Division
from ..election import Election


class ContestBase(OCDBase):
    """
    A base class for representing a specific decision set before voters in an election.

    Includes properties shared by all contest types: BallotMeasureContest,
    CandidateContest, PartyContest and RetentionContest.
    """

    id = OCDIDField(
        ocd_type="contest",
        help_text="Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.",
    )
    name = models.CharField(
        max_length=300,
        help_text="Name of the contest, not necessarily as it appears on the ballot.",
    )
    division = models.ForeignKey(
        Division,
        related_name="%(class)ss",
        related_query_name="%(class)ss",
        help_text="Reference to the Division that defines the political "
        "geography of the contest, e.g., a specific Congressional or "
        "State Senate district. Should be a subdivision of the Division "
        "referenced by the contest's Election.",
        on_delete=models.PROTECT,
    )
    election = models.ForeignKey(
        Election,
        related_name="%(class)ss",
        related_query_name="%(class)ss",
        help_text="Reference to the Election in which the contest is decided.",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0} (in {1})".format(self.name, self.election.name)

    class Meta:
        """
        Model options.
        """

        ordering = ("election", "name")
        abstract = True
