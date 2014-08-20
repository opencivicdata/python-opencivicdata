from django.contrib import admin
from opencivicdata import models
from . import base


class LegislativeSessionInline(base.NoAddTabularInline):
    model = models.LegislativeSession
    readonly_fields = ('identifier', 'name', 'classification')
    can_delete = False


@admin.register(models.Jurisdiction)
class JurisdictionAdmin(base.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields = fields = ('id', 'name', 'classification', 'url', 'division', 'feature_flags',
                                'extras')
    inlines = [LegislativeSessionInline]
