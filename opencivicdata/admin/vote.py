from django.contrib import admin
from opencivicdata.models import vote as models


@admin.register(models.VoteEvent)
class VoteEventAdmin(admin.ModelAdmin):
    pass

@admin.register(models.VoteCount)
class VoteCountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.PersonVote)
class PersonVoteAdmin(admin.ModelAdmin):
    pass

@admin.register(models.VoteSource)
class VoteSourceAdmin(admin.ModelAdmin):
    pass

