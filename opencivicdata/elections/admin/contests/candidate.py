#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for OpenCivicData election contest models.
"""
from django.contrib import admin
from opencivicdata.core.admin import base
from ... import models


class CandidateContestIdentifierInline(base.IdentifierInline):
    """
    Custom inline administrative panel for CandidateContestIdentifier model.
    """

    model = models.CandidateContestIdentifier


class CandidateContestSourceInline(base.LinkInline):
    """
    Custom inline administrative panel for the CandidateContestSource model.
    """

    model = models.CandidateContestSource


class CandidateContestPostInline(admin.TabularInline):
    """
    Custom administrative panel for CandidateContestPost model.
    """

    model = models.CandidateContestPost
    extra = 0


@admin.register(models.CandidateContest)
class CandidateContestAdmin(base.ModelAdmin):
    """
    Custom administrative panel for the CandidateContest model.
    """

    readonly_fields = ("id", "created_at", "updated_at")
    raw_id_fields = ("division", "runoff_for_contest")
    fields = (
        ("name", "election", "party", "previous_term_unexpired", "number_elected")
        + raw_id_fields
        + readonly_fields
    )
    list_display = ("name", "election", "division_name", "id", "updated_at")
    search_fields = ("name", "election__name")
    list_filter = ("updated_at",)
    date_hierarchy = "election__date"

    inlines = [
        CandidateContestPostInline,
        CandidateContestIdentifierInline,
        CandidateContestSourceInline,
    ]

    def division_name(self, obj):
        """
        Returns the name of the Division for the Contest.
        """
        return obj.division.name
