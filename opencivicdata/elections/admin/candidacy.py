#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for Candidacy-related models.
"""
from django import VERSION as django_version
from django.contrib import admin
from opencivicdata.core.admin import base
from .. import models


class CandidacySourceInline(base.LinkInline):
    """
    Custom inline administrative panel for the CandidacySource model.
    """
    model = models.CandidacySource


@admin.register(models.Candidacy)
class CandidacyAdmin(base.ModelAdmin):
    """
    Custom inline administrative panel for the Candidacy model.
    """
    raw_id_fields = (
        'person',
        'contest',
        'top_ticket_candidacy',
    )
    fields = (
        'candidate_name',
        'post',
        'filed_date',
        'is_incumbent',
        'registration_status',
        'party',
    ) + raw_id_fields
    list_display = (
        'candidate_name',
        'contest',
        'is_incumbent',
        'registration_status',
        'id',
        'party__name',
        'updated_at',
    )

    search_fields = ('candidate_name', 'contest__name', 'post__label', )
    list_filter = (
        'party__name',
        'is_incumbent',
        'registration_status',
        'updated_at',
    )
    # date_hierarchy across relations was added to django 1.11
    if django_version[0] >= 1 and django_version[1] >= 11:
        date_hierarchy = 'contest__election__start_time'

    inlines = [
        CandidacySourceInline,
    ]
