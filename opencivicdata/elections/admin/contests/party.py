#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for OpenCivicData election contest models.
"""
from django.contrib import admin
from opencivicdata.core.admin import base
from ... import models


class PartyContestIdentifierInline(base.IdentifierInline):
    """
    Custom inline administrative panel for PartyContestIdentifier model.
    """

    model = models.PartyContestIdentifier


class PartyContestSourceInline(base.LinkInline):
    """
    Custom inline administrative panel for the PartyContestSource model.
    """

    model = models.PartyContestSource


class PartyContestOptionInline(admin.TabularInline):
    """
    Custom administrative panel for PartyContestOption model.
    """

    model = models.PartyContestOption
    extra = 0


@admin.register(models.PartyContest)
class PartyContestAdmin(base.ModelAdmin):
    """
    Custom administrative panel for the PartyContest model.
    """

    readonly_fields = ("id", "created_at", "updated_at")
    raw_id_fields = ("division", "runoff_for_contest")
    fields = ("name", "election") + raw_id_fields + readonly_fields
    list_display = ("name", "election", "id", "updated_at")
    search_fields = ("name", "election__name")
    list_filter = ("updated_at",)
    date_hierarchy = "election__date"

    inlines = [
        PartyContestOptionInline,
        PartyContestIdentifierInline,
        PartyContestSourceInline,
    ]
