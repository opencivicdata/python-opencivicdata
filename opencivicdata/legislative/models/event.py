from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from opencivicdata.core.models.base import (
    OCDBase,
    LinkBase,
    OCDIDField,
    RelatedBase,
    RelatedEntityBase,
    MimetypeLinkBase,
)
from opencivicdata.core.models import Jurisdiction
from .bill import Bill
from .vote import VoteEvent
from ...common import (
    EVENT_MEDIA_CLASSIFICATION_CHOICES,
    EVENT_DOCUMENT_CLASSIFICATION_CHOICES,
)

EVENT_STATUS_CHOICES = (
    ("cancelled", "Cancelled"),
    ("tentative", "Tentative"),
    ("confirmed", "Confirmed"),
    ("passed", "Passed"),
)


class EventMediaBase(RelatedBase):
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=25, blank=True)  # YYYY-MM-DD HH:MM:SS+HH:MM
    offset = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True


class EventLocation(RelatedBase):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, max_length=2000)
    coordinates = models.PointField(null=True)
    jurisdiction = models.ForeignKey(
        Jurisdiction, related_name="event_locations", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "opencivicdata_eventlocation"


class Event(OCDBase):
    id = OCDIDField(ocd_type="event")
    name = models.CharField(max_length=1000)
    jurisdiction = models.ForeignKey(
        Jurisdiction,
        related_name="events",
        # jurisdictions hard to delete
        on_delete=models.PROTECT,
    )
    description = models.TextField()
    classification = models.CharField(max_length=100)
    start_date = models.CharField(max_length=25)  # YYYY-MM-DD HH:MM:SS+HH:MM
    end_date = models.CharField(max_length=25, blank=True)  # YYYY-MM-DD HH:MM:SS+HH:MM
    all_day = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES)
    location = models.ForeignKey(EventLocation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.start_date)

    class Meta:
        db_table = "opencivicdata_event"
        index_together = [["jurisdiction", "start_date", "name"]]


class EventMedia(EventMediaBase):
    event = models.ForeignKey(Event, related_name="media", on_delete=models.CASCADE)
    classification = models.CharField(
        max_length=50, choices=EVENT_MEDIA_CLASSIFICATION_CHOICES, blank=True
    )

    def __str__(self):
        return "%s for %s" % (self.note, self.event)

    class Meta:
        db_table = "opencivicdata_eventmedia"


class EventMediaLink(MimetypeLinkBase):
    media = models.ForeignKey(
        EventMedia, related_name="links", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} for {1}".format(self.url, self.media.event)

    class Meta:
        db_table = "opencivicdata_eventmedialink"


class EventDocument(RelatedBase):
    event = models.ForeignKey(Event, related_name="documents", on_delete=models.CASCADE)
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=25, blank=True)  # YYYY-MM-DD HH:MM:SS+HH:MM
    classification = models.CharField(
        max_length=50, choices=EVENT_DOCUMENT_CLASSIFICATION_CHOICES, blank=True
    )

    def __str__(self):
        tmpl = "{doc.note} for event {doc.event}"
        return tmpl.format(doc=self)

    class Meta:
        db_table = "opencivicdata_eventdocument"


class EventDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(
        EventDocument, related_name="links", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} for {1}".format(self.url, self.document)

    class Meta:
        db_table = "opencivicdata_eventdocumentlink"


class EventLink(LinkBase):
    event = models.ForeignKey(Event, related_name="links", on_delete=models.CASCADE)

    class Meta:
        db_table = "opencivicdata_eventlink"


class EventSource(LinkBase):
    event = models.ForeignKey(Event, related_name="sources", on_delete=models.CASCADE)

    class Meta:
        db_table = "opencivicdata_eventsource"


class EventParticipant(RelatedEntityBase):
    event = models.ForeignKey(
        Event, related_name="participants", on_delete=models.CASCADE
    )
    note = models.TextField()

    def __str__(self):
        tmpl = "%s at %s"
        return tmpl % (self.name, self.event)

    class Meta:
        db_table = "opencivicdata_eventparticipant"


class EventAgendaItem(RelatedBase):
    description = models.TextField()
    classification = ArrayField(base_field=models.TextField(), blank=True, default=list)
    order = models.CharField(max_length=100, blank=True)
    subjects = ArrayField(base_field=models.TextField(), blank=True, default=list)
    notes = ArrayField(base_field=models.TextField(), blank=True, default=list)
    event = models.ForeignKey(Event, related_name="agenda", on_delete=models.CASCADE)
    extras = JSONField(default=dict, blank=True)

    def __str__(self):
        return "Agenda item {0} for {1}".format(self.order, self.event).replace(
            "  ", " "
        )

    class Meta:
        db_table = "opencivicdata_eventagendaitem"


class EventRelatedEntity(RelatedEntityBase):
    agenda_item = models.ForeignKey(
        EventAgendaItem, related_name="related_entities", on_delete=models.CASCADE
    )
    # will just unresolve if needed
    bill = models.ForeignKey(Bill, null=True, on_delete=models.SET_NULL)
    vote_event = models.ForeignKey(VoteEvent, null=True, on_delete=models.SET_NULL)
    note = models.TextField()

    def __str__(self):
        return "{0} related to {1}".format(self.entity_name, self.agenda_item)

    @property
    def entity_name(self):
        if self.entity_type == "vote" and self.vote_event_id:
            return self.vote_event.identifier
        elif self.entity_type == "bill" and self.bill_id:
            return self.bill.identifier
        else:
            return super(EventRelatedEntity, self).entity_name

    @property
    def entity_id(self):
        if self.entity_type == "vote":
            return self.vote_event_id
        if self.entity_type == "bill":
            return self.bill_id
        return super(EventRelatedEntity, self).entity_id

    class Meta:
        db_table = "opencivicdata_eventrelatedentity"


class EventAgendaMedia(EventMediaBase):
    agenda_item = models.ForeignKey(
        EventAgendaItem, related_name="media", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} for {1}".format(self.note, self.agenda_item)

    class Meta:
        db_table = "opencivicdata_eventagendamedia"


class EventAgendaMediaLink(MimetypeLinkBase):
    media = models.ForeignKey(
        EventAgendaMedia, related_name="links", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} for {1}".format(self.url, self.media)

    class Meta:
        db_table = "opencivicdata_eventagendamedialink"
