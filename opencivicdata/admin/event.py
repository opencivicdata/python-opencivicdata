from django.contrib import admin
from opencivicdata.models import event as models


@admin.register(models.EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


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

