#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PartyContest-related models.
"""
from django.db import models
from opencivicdata.core.models.base import IdentifierBase, LinkBase
from opencivicdata.core.models import Organization
from .base import ContestBase


class PartyContest(ContestBase):
    """
    A contest in which voters can vote directly for a political party.

    In these contests, voters can vote for a party in lieu of/in addition to
    voting for candidates endorsed by that party (as in the case of party-list
    proportional representation).
    """

    runoff_for_contest = models.OneToOneField(
        "self",
        null=True,
        on_delete=models.SET_NULL,
        help_text="If this contest is a runoff to determine the outcome of a previously "
        "undecided contest, reference to that PartyContest.",
    )

    class Meta:
        db_table = "opencivicdata_partycontest"


class PartyContestOption(models.Model):
    """
    A party (i.e., Organization) voters choose in a PartyContest.
    """

    contest = models.ForeignKey(
        PartyContest,
        related_name="parties",
        on_delete=models.CASCADE,
        help_text="Reference to the PartyContest in which the party is an option.",
    )
    party = models.ForeignKey(
        Organization,
        related_name="party_contests",
        on_delete=models.CASCADE,
        limit_choices_to={"classification": "party"},
        help_text="Reference to an Organization representing a political party "
        "voters may choose in the contest.",
    )
    is_incumbent = models.NullBooleanField(
        help_text="Indicates whether the party currently holds majority power."
    )

    def __str__(self):
        return "{0} for {1}".format(self.party.name, self.contest)

    class Meta:
        """
        Model options.
        """

        db_table = "opencivicdata_partycontestoption"
        ordering = ("contest", "party")


class PartyContestIdentifier(IdentifierBase):
    """
    Upstream identifiers of a PartyMeasureContest.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """

    contest = models.ForeignKey(
        PartyContest,
        related_name="identifiers",
        on_delete=models.CASCADE,
        help_text="Reference to the PartyContest linked to the upstream " "identifier.",
    )

    def __str__(self):
        tmpl = "%s identifies %s"
        return tmpl % (self.identifier, self.contest)

    class Meta:
        db_table = "opencivicdata_partyidentifier"


class PartyContestSource(LinkBase):
    """
    Source used in assembling a PartyContest.
    """

    contest = models.ForeignKey(
        PartyContest,
        related_name="sources",
        on_delete=models.CASCADE,
        help_text="Reference to the PartyContest assembled from the source.",
    )

    class Meta:
        db_table = "opencivicdata_partysource"
