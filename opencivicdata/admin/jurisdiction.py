from django.contrib import admin
from opencivicdata.models import jurisdiction as models


@admin.register(models.LegislativeSession)
class LegislativeSessionAdmin(admin.TabularInline):
    pass


@admin.register(models.Jurisdiction)
class JurisdictionAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'jurisdiction', 'extras', 'feature_flags']
    inlines = [LegislativeSessionAdmin]

