#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PartyContest-related models.
"""
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from opencivicdata.core.models.base import IdentifierBase, LinkBase
from opencivicdata.core.models import Organization
from .base import ContestBase


class PartyContest(ContestBase):
    """
    Subclass of Contest wherein voters can vote directly for a political party.
    """
    runoff_for_contest = models.OneToOneField(
        'self',
        null=True,
        help_text="If this contest is a runoff to determine the outcome of a previously "
                  "undecided contest, reference to that PartyContest.",
    )

    class Meta:
        db_table = 'opencivicdata_partycontest'


@python_2_unicode_compatible
class PartyContestOption(models.Model):
    """
    Link between a PartyContest and a Party for which a voter could vote in the election contest.
    """
    contest = models.ForeignKey(
        PartyContest,
        related_name="parties",
        help_text="Reference to the PartyContest in which the Party is an option.",
    )
    party = models.ForeignKey(
        Organization,
        related_name='party_contests',
        limit_choices_to={'classification': 'party'},
        help_text="Reference to the Party option in the PartyContest.",
    )
    is_incumbent = models.NullBooleanField(
        help_text="Indicates whether the party currently holds majority power.",
    )

    def __str__(self):
        return "{0} for {1}".format(self.party.name, self.contest)

    class Meta:
        """
        Model options.
        """
        db_table = 'opencivicdata_partycontestoption'
        ordering = ("contest", "party",)


@python_2_unicode_compatible
class PartyContestIdentifier(IdentifierBase):
    """
    Upstream identifiers of the PartyMeasureContest, if any exist.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """
    contest = models.ForeignKey(
        PartyContest,
        related_name="identifiers",
        help_text="Reference to the PartyContest linked to the upstream "
                  "identifier.",
    )

    def __str__(self):
        tmpl = '%s identifies %s'
        return tmpl % (self.identifier, self.contest)

    class Meta:
        db_table = 'opencivicdata_partyidentifier'


class PartyContestSource(LinkBase):
    """
    Source used in assembling the PartyContest.
    """
    contest = models.ForeignKey(
        PartyContest,
        related_name='sources',
        help_text="Reference to the PartyContest assembled from the source.",
    )

    class Meta:
        db_table = 'opencivicdata_partysource'
