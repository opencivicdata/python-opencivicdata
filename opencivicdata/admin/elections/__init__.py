#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for OpenCivicData election models.
"""
from django import VERSION as django_version
from django.core import urlresolvers
from django.contrib import admin
from django.utils.html import format_html, mark_safe
from ... import models
from ..event import EventSourceInline
from ..base import (ModelAdmin, ReadOnlyTabularInline, IdentifierInline, LinkInline,
                   ContactDetailInline, OtherNameInline)


class ElectionIdentifierInline(IdentifierInline):
    """
    Custom administrative panel for the ElectionIdentifier model.
    """
    model = models.ElectionIdentifier


@admin.register(models.Election)
class ElectionAdmin(ModelAdmin):
    """
    Custom administrative panel for the Election model.
    """
    readonly_fields = (
        'created_at',
        'updated_at',
        'event_link',
    )
    raw_id_fields = ('division', )
    fields = (
        'name',
        'start_time',
        'administrative_organization',
        'extras',
    ) + raw_id_fields + readonly_fields
    search_fields = ('name', )
    list_filter = ('updated_at', )
    date_hierarchy = 'start_time'
    list_display = ('name', 'date', 'id', 'updated_at', )
    ordering = ('-start_time', )

    inlines = [
        ElectionIdentifierInline,
        EventSourceInline,
    ]

    def date(self, obj):
        """
        Return start_time of the Event as a date.
        """
        return obj.start_time.date()
    date.admin_order_field = 'start_time'

    def event_link(self, obj):
        """
        Return a link to the event's admin page.
        """
        link = urlresolvers.reverse(
            "admin:opencivicdata_event_change",
            args=[obj.id]
        )
        
        return format_html(
            '<a href="{0}" target="_blank">{1}</a>',
            link,
            obj.id,
        )
    event_link.short_description = 'id'


class CandidacySourceInline(LinkInline):
    """
    Custom administrative panel for the CandidacySource model.
    """
    model = models.CandidacySource


@admin.register(models.Candidacy)
class CandidacyAdmin(ModelAdmin):
    """
    Custom administrative panel for the Candidacy model.
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
        'party_abbreviation',
        'updated_at',
    )
    
    search_fields = ('candidate_name', 'contest__name', 'post__label', )
    list_filter = (
        'party',
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
    
    def party_abbreviation(self, obj):
        """
        Return the abbreviation of the party associated with the Candidacy.
        """
        if obj.party:
            abbrv = obj.party.abbreviation
        else:
            abbrv = None
        return abbrv
    party_abbreviation.short_description = 'Party'


@admin.register(models.Party)
class PartyAdmin(ModelAdmin):
    """
    Custom administrative panel for the Party model.
    """
    readonly_fields = (
        'created_at',
        'updated_at',
        'org_link',
    )
    fields = (
        'name',
        'abbreviation',
        'color',
        'is_write_in',
    )
    list_display = (
        'name',
        'abbreviation',
        'id',
        'updated_at',
    )
    search_fields = ('name', )
    list_filter = ('updated_at', 'abbreviation', )

    def org_link(self, obj):
        """
        Return a link to the event's admin page.
        """
        link = urlresolvers.reverse(
            "admin:opencivicdata_organization_change",
            args=[obj.id]
        )
        
        return format_html(
            '<a href="{0}" target="_blank">{1}</a>',
            link,
            obj.id,
        )
    org_link.short_description = 'id'
