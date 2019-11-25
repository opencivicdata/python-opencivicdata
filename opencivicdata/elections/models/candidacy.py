#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Candidacy-related models.
"""
from django.db import models
from opencivicdata.core.models.base import OCDBase, LinkBase, OCDIDField
from opencivicdata.core.models import Person, Post, Organization


class Candidacy(OCDBase):
    """
    A person seeking election to hold a specific public office for a term.
    """

    id = OCDIDField(
        ocd_type="candidacy",
        help_text="Open Civic Data-style id in the format ``ocd-candidacy/{{uuid}}``.",
    )
    person = models.ForeignKey(
        Person,
        related_name="candidacies",
        help_text="Reference to the Person who is the candidate.",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        related_name="candidacies",
        help_text="Reference to Post representing the public office for which "
        "the candidate is seeking election.",
        on_delete=models.PROTECT,
    )
    contest = models.ForeignKey(
        "elections.CandidateContest",
        related_name="candidacies",
        help_text="Reference to an OCD CandidateContest representing the contest "
        "in which the candidate is competing.",
        on_delete=models.CASCADE,
    )
    candidate_name = models.CharField(
        max_length=300,
        help_text="For preserving the candidate's name as it was of the candidacy.",
    )
    filed_date = models.DateField(
        null=True, help_text="Specifies when the candidate filed for the contest."
    )
    is_incumbent = models.NullBooleanField(
        help_text="Indicates whether the candidate is seeking re-election to a "
        "public office he/she currently holds"
    )
    party = models.ForeignKey(
        Organization,
        related_name="candidacies",
        limit_choices_to={"classification": "party"},
        null=True,
        help_text="Reference to the Organization representing the political party "
        "that nominated the candidate or would nominate the candidate "
        "(as in the case of a partisan primary).",
        # survive party deletion
        on_delete=models.SET_NULL,
    )
    REGISTRATION_STATUSES = (
        ("filed", "Filed"),
        ("qualified", "Qualified"),
        ("withdrawn", "Withdrawn"),
        ("write-in", "Write-in"),
    )
    registration_status = models.CharField(
        max_length=10,
        choices=REGISTRATION_STATUSES,
        null=True,
        help_text="Registration status of the candidate.",
    )
    top_ticket_candidacy = models.ForeignKey(
        "self",
        related_name="ticket",
        null=True,
        on_delete=models.SET_NULL,
        help_text="If the candidate is running as part of ticket, e.g., a Vice "
        "Presidential candidate running with a Presidential candidate, "
        "reference to candidacy at the top of the ticket.",
    )

    def __str__(self):
        return "{0.candidate_name} for {0.contest}".format(self)

    class Meta:
        """
        Model options.
        """

        db_table = "opencivicdata_candidacy"
        verbose_name_plural = "candidacies"
        ordering = ("contest", "post", "person")

    @property
    def election(self):
        """
        Election in which the person is a candidate.
        """
        return self.contest.election


class CandidacySource(LinkBase):
    """
    Source used in assembling a Candidacy.
    """

    candidacy = models.ForeignKey(
        Candidacy,
        related_name="sources",
        on_delete=models.CASCADE,
        help_text="Reference to the assembed Candidacy.",
    )

    class Meta:
        db_table = "opencivicdata_candidacysource"
