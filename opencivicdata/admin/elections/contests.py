#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for OpenCivicData election contest models.
"""
from django import VERSION as django_version
from django.contrib import admin
from ... import models
from ..base import (ModelAdmin, ReadOnlyTabularInline, IdentifierInline, LinkInline,
                   ContactDetailInline, OtherNameInline)


class ContestIdentifierInline(IdentifierInline):
    """
    Custom administrative panel for ContestIdentifier model.
    """
    model = models.ContestIdentifier


class ContestSourceInline(LinkInline):
    """
    Custom administrative panel for the ContestSource model.
    """
    model = models.ContestSource


@admin.register(models.ContestBase)
class ContestBaseAdmin(ModelAdmin):
    """
    Custom administrative panel for the ContestBase model.
    """
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('division', )
    fields = (
        'name',
        'election',
    ) + raw_id_fields + readonly_fields
    list_display = (
        'name',
        'election',
        'division_name',
        'id',
        'updated_at',
    )
    search_fields = ('name', 'election__name', )
    list_filter = ('updated_at', )
    # date_hierarchy across relations was added to django 1.11
    if django_version[0] >= 1 and django_version[1] >= 11:
        date_hierarchy = 'election__start_time'

    inlines = [
        ContestIdentifierInline,
        ContestSourceInline,
    ]

    def division_name(self, obj):
        """
        Returns the name of the Division for the Contest.
        """
        return obj.division.name


class BallotMeasureContestOptionInline(admin.TabularInline):
    """
    Custom administrative panel for BallotMeasureContestOption model.
    """
    model = models.BallotMeasureContestOption
    extra = 0


@admin.register(models.BallotMeasureContest)
class BallotMeasureContestBaseAdmin(ModelAdmin):
    """
    Custom administrative panel for the BallotMeasureContest model.
    """
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('division', 'runoff_for_contest', )
    fields = (
        'name',
        'description',
        'requirement',
        'classification',
        'election',
    ) + raw_id_fields + readonly_fields
    list_display = (
        'name',
        'election',
        'id',
        'updated_at',
    )
    search_fields = ('name', 'election__name', )
    list_filter = ('classification', 'updated_at', )
    # date_hierarchy across relations was added to django 1.11
    if django_version[0] >= 1 and django_version[1] >= 11:
        date_hierarchy = 'election__start_time'

    inlines = [
        BallotMeasureContestOptionInline,
        ContestIdentifierInline,
        ContestSourceInline,
    ]


@admin.register(models.RetentionContest)
class RetentionContestBaseAdmin(ModelAdmin):
    """
    Custom administrative panel for the RetentionContest model.
    """
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('membership', 'division', 'runoff_for_contest', )
    fields = (
        'name',
        'description',
        'requirement',
        'classification',
        'election',
    ) + raw_id_fields + readonly_fields
    list_display = (
        'name',
        'membership',
        'election',
        'id',
        'updated_at',
    )
    search_fields = (
        'name',
        'membership__person__name',
        'membership__role',
        'election__name',
    )
    list_filter = ('classification', 'updated_at', )
    # date_hierarchy across relations was added to django 1.11
    if django_version[0] >= 1 and django_version[1] >= 11:
        date_hierarchy = 'election__start_time'

    inlines = [
        BallotMeasureContestOptionInline,
        ContestIdentifierInline,
        ContestSourceInline,
    ]


class CandidateContestPostInline(admin.TabularInline):
    """
    Custom administrative panel for CandidateContestPost model.
    """
    model = models.CandidateContestPost
    extra = 0


@admin.register(models.CandidateContest)
class CandidateContestBaseAdmin(ModelAdmin):
    """
    Custom administrative panel for the CandidateContest model.
    """
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('division', 'runoff_for_contest', )
    fields = (
        'name',
        'election',
        'party',
        'previous_term_unexpired',
        'number_elected',
    ) + raw_id_fields + readonly_fields
    list_display = (
        'name',
        'election',
        'division_name',
        'id',
        'updated_at',
    )
    search_fields = ('name', 'election__name', )
    list_filter = ('updated_at', )
    # date_hierarchy across relations was added to django 1.11
    if django_version[0] >= 1 and django_version[1] >= 11:
        date_hierarchy = 'election__start_time'

    inlines = [
        CandidateContestPostInline,
        ContestIdentifierInline,
        ContestSourceInline,
    ]

    def division_name(self, obj):
        """
        Returns the name of the Division for the Contest.
        """
        return obj.division.name


class PartyContestOptionInline(admin.TabularInline):
    """
    Custom administrative panel for PartyContestOption model.
    """
    model = models.PartyContestOption
    extra = 0


@admin.register(models.PartyContest)
class PartyContestBaseAdmin(ModelAdmin):
    """
    Custom administrative panel for the PartyContest model.
    """
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('division', 'runoff_for_contest', )
    fields = (
        'name',
        'election',
    ) + raw_id_fields + readonly_fields
    list_display = (
        'name',
        'election',
        'id',
        'updated_at',
    )
    search_fields = ('name', 'election__name', )
    list_filter = ('updated_at', )
    # date_hierarchy across relations was added to django 1.11
    if django_version[0] >= 1 and django_version[1] >= 11:
        date_hierarchy = 'election__start_time'

    inlines = [
        PartyContestOptionInline,
        ContestIdentifierInline,
        ContestSourceInline,
    ]