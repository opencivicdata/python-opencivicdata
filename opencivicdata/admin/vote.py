from django.contrib import admin
from opencivicdata.models import vote as models



class VoteCountInline(admin.TabularInline):
    model = models.VoteCount
    fields = readonly_fields = ('option', 'value')
    extra = 0


class PersonVoteInline(admin.TabularInline):
    model = models.PersonVote
    fields = readonly_fields = (
        'voter', 'voter_name', 'option')
    extra = 0


class VoteSourceInline(admin.TabularInline):
    model = models.VoteSource
    fields = readonly_fields = ('url', 'note')
    extra = 0


@admin.register(models.VoteEvent)
class VoteEventAdmin(admin.ModelAdmin):
    readonly_fields = (
        'bill', 'organization', 'legislative_session', 'id')
    fields = (
        'organization', 'legislative_session', 'bill',
        'result', 'id', 'identifier', 'motion_text',
        'motion_classification', 'start_date', 'end_date',
        'extras')

    list_selected_related = (
        'sources',
        'legislative_session',
        'legislative_session__jurisdiction')

    inlines = [
        VoteCountInline, PersonVoteInline,
        VoteSourceInline]


@admin.register(models.VoteCount)
class VoteCountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonVote)
class PersonVoteAdmin(admin.ModelAdmin):
    list_display = ('voter_name', 'vote')
    readonly_fields = ('vote',)


@admin.register(models.VoteSource)
class VoteSourceAdmin(admin.ModelAdmin):
    pass

