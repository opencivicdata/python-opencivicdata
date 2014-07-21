from django.contrib import admin
from django.template import defaultfilters
from opencivicdata.models import event as models


@admin.register(models.EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
   pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('jurisdiction', 'location')
    fields = (
        'name', 'jurisdiction', 'location', 'description',
        'classification', 'status',
        ('start_time', 'end_time'),
        ('timezone', 'all_day'),
        )

    def source_link(self, obj):
        source = obj.sources.filter(url__icontains="meetingdetail").get()
        tmpl = u'<a href="{0}" target="_blank">View source</a>'
        return tmpl.format(source.url)
    source_link.short_description = 'View source'
    source_link.allow_tags = True

    list_display = (
        'jurisdiction', 'name', 'start_time', 'source_link')


@admin.register(models.EventMedia)
class EventMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventMediaLink)
class EventMediaLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventDocument)
class EventDocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventDocumentLink)
class EventDocumentLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventLink)
class EventLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventSource)
class EventSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventAgendaItem)
class EventAgendaItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventRelatedEntity)
class EventRelatedEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventAgendaMedia)
class EventAgendaMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventAgendaMediaLink)
class EventAgendaMediaLinkAdmin(admin.ModelAdmin):
    pass

