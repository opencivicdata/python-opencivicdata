#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for Election-related models.
"""
from django.contrib import admin
from opencivicdata.core.admin import base
from .. import models


class ElectionSourceInline(base.LinkInline):
    """
    Custom inline administrative panely for ElectionSource model.
    """

    model = models.ElectionSource


class ElectionIdentifierInline(base.IdentifierInline):
    """
    Custom inline administrative panel for the ElectionIdentifier model.
    """

    model = models.ElectionIdentifier


@admin.register(models.Election)
class ElectionAdmin(base.ModelAdmin):
    """
    Custom inline administrative panel for the Election model.
    """

    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("division",)
    fields = (
        ("name", "date", "administrative_organization", "extras")
        + raw_id_fields
        + readonly_fields
    )
    search_fields = ("name",)
    list_filter = ("updated_at",)
    date_hierarchy = "date"
    list_display = ("name", "date", "id", "updated_at")
    ordering = ("-date",)

    inlines = [ElectionIdentifierInline, ElectionSourceInline]
