#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for OpenCivicData election contest models.
"""
from django.contrib import admin
from opencivicdata.core.admin import base
from ... import models


class BallotMeasureContestIdentifierInline(base.IdentifierInline):
    """
    Custom inline administrative panel for BallotMeasureContestIdentifier model.
    """

    model = models.BallotMeasureContestIdentifier


class BallotMeasureContestSourceInline(base.LinkInline):
    """
    Custom inline administrative panel for the BallotMeasureContestSource model.
    """

    model = models.BallotMeasureContestSource


class BallotMeasureContestOptionInline(admin.TabularInline):
    """
    Custom inline administrative panel for BallotMeasureContestOption model.
    """

    model = models.BallotMeasureContestOption
    extra = 0


@admin.register(models.BallotMeasureContest)
class BallotMeasureContestAdmin(base.ModelAdmin):
    """
    Custom administrative panel for the BallotMeasureContest model.
    """

    readonly_fields = ("id", "created_at", "updated_at")
    raw_id_fields = ("division",)
    fields = (
        ("name", "election", "description", "requirement", "classification")
        + raw_id_fields
        + readonly_fields
    )
    list_display = ("name", "election", "division_name", "id", "updated_at")
    search_fields = ("name", "election__name")
    list_filter = ("updated_at", "classification")
    date_hierarchy = "election__date"

    def division_name(self, obj):
        """
        Returns the name of the Division for the Contest.
        """
        return obj.division.name

    inlines = [
        BallotMeasureContestOptionInline,
        BallotMeasureContestIdentifierInline,
        BallotMeasureContestSourceInline,
    ]


class RetentionContestIdentifierInline(base.IdentifierInline):
    """
    Custom inline administrative panel for RetentionContestIdentifier model.
    """

    model = models.RetentionContestIdentifier


class RetentionContestSourceInline(base.LinkInline):
    """
    Custom inline administrative panel for the RetentionContestSource model.
    """

    model = models.RetentionContestSource


class RetentionContestOptionInline(admin.TabularInline):
    """
    Custom inline administrative panel for RetentionContestOption model.
    """

    model = models.RetentionContestOption
    extra = 0


@admin.register(models.RetentionContest)
class RetentionContestBaseAdmin(base.ModelAdmin):
    """
    Custom administrative panel for the RetentionContest model.
    """

    readonly_fields = ("id", "created_at", "updated_at")
    raw_id_fields = ("membership", "division", "runoff_for_contest")
    fields = (
        ("name", "description", "requirement", "election")
        + raw_id_fields
        + readonly_fields
    )
    list_display = ("name", "membership", "election", "id", "updated_at")
    search_fields = (
        "name",
        "membership__person__name",
        "membership__role",
        "election__name",
    )
    list_filter = ("updated_at",)
    date_hierarchy = "election__date"

    inlines = [
        RetentionContestOptionInline,
        RetentionContestIdentifierInline,
        RetentionContestSourceInline,
    ]
