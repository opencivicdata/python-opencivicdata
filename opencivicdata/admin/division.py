from django.contrib import admin
from opencivicdata import models
from . import base


@admin.register(models.Division)
class DivisionAdmin(base.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = list_display
    fields = readonly_fields = ('id', 'name', 'redirect', 'country')
