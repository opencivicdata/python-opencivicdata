from django.contrib import admin
from opencivicdata.models import jurisdiction as models


@admin.register(models.Jurisdiction)
class JurisdictionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LegislativeSession)
class LegislativeSessionAdmin(admin.ModelAdmin):
    pass

