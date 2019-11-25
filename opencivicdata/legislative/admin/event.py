from django.contrib import admin
from django.template import defaultfilters
from opencivicdata.core.admin import base
from .. import models


@admin.register(models.EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
    pass


class EventLinkInline(base.LinkInline):
    model = models.EventLink


class EventSourceInline(base.LinkInline):
    model = models.EventSource


class EventParticipantInline(base.RelatedEntityInline):
    model = models.EventParticipant
    readonly_fields = ("organization", "person")


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ("jurisdiction", "location")
    fields = (
        "name",
        "jurisdiction",
        "location",
        "description",
        "classification",
        "status",
        ("start_date", "end_date", "all_day"),
    )

    def source_link(self, obj):
        source = obj.sources.filter(url__icontains="meetingdetail").get()
        tmpl = u'<a href="{0}" target="_blank">View source</a>'
        return tmpl.format(source.url)

    source_link.short_description = "View source"
    source_link.allow_tags = True

    list_display = ("jurisdiction", "name", "start_date", "source_link")

    inlines = [EventLinkInline, EventSourceInline, EventParticipantInline]


@admin.register(models.EventMedia)
class EventMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventDocument)
class EventDocumentAdmin(admin.ModelAdmin):
    readonly_fields = ("event",)
    list_display = ("event", "date", "note")


# @admin.register(models.EventDocumentLink)
# class EventDocumentLinkAdmin(base.MimetypeLinkAdmin):
#    readonly_fields = ('document',)
#    list_display = ('document', 'media_type', 'url',)


@admin.register(models.EventSource)
class EventSourceAdmin(admin.ModelAdmin):
    readonly_fields = ("event",)


@admin.register(models.EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventAgendaItem)
class EventAgendaItemAdmin(admin.ModelAdmin):
    readonly_fields = ("event",)
    fields = ("event", "description", "classification", "order", "subjects", "notes")

    def get_truncated_description(self, obj):
        return defaultfilters.truncatewords(obj.description, 25)

    get_truncated_description.short_description = "Description"

    def get_truncated_event_name(self, obj):
        return defaultfilters.truncatewords(obj.event.name, 8)

    get_truncated_event_name.short_description = "Event Name"

    list_display = ("get_truncated_event_name", "get_truncated_description")


@admin.register(models.EventRelatedEntity)
class EventRelatedEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventAgendaMedia)
class EventAgendaMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventAgendaMediaLink)
class EventAgendaMediaLinkAdmin(admin.ModelAdmin):
    pass
