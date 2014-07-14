from django.contrib import admin
from opencivicdata.models import division as models


@admin.register(models.Division)
class DivisionAdmin(admin.ModelAdmin):
    pass

