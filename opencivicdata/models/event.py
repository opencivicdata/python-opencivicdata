from django.contrib.gis.db import models
from djorm_pgarray.fields import ArrayField
from .base import OCDBase, LinkBase, OCDIDField, RelatedBase, MimetypeLinkBase, RelatedEntityBase
from .jurisdiction import Jurisdiction
from .bill import Bill
from .vote import VoteEvent


EVENT_STATUS_CHOICES = (
    ('cancelled', 'Cancelled'),
    ('tentative', 'Tentative'),
    ('confirmed', 'Confirmed'),
    ('passed', 'Passed'),
)


class EventMediaBase(RelatedBase):
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    offset = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True


class EventLocation(RelatedBase):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, max_length=2000)
    coordinates = models.PointField(null=True)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='event_locations')

    objects = models.GeoManager()

    def __str__(self):
        return self.name


class Event(OCDBase):
    id = OCDIDField(ocd_type='event')
    name = models.CharField(max_length=300)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='events')
    description = models.TextField()
    classification = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    timezone = models.CharField(max_length=300)
    end_time = models.DateTimeField(null=True)
    all_day = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES)
    location = models.ForeignKey(EventLocation, null=True)

    def __str__(self):
        return self.name

    class Meta:
        index_together = [
            ['jurisdiction', 'start_time', 'name']
        ]

class EventMedia(EventMediaBase):
    event = models.ForeignKey(Event, related_name='media')

    def __str__(self):
        return '%s for %s' % (self.note, self.event)


class EventMediaLink(MimetypeLinkBase):
    media = models.ForeignKey(EventMedia, related_name='links')


class EventDocument(MimetypeLinkBase):
    event = models.ForeignKey(Event, related_name='documents')
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10)

    def __str__(self):
        tmpl = '{doc.note} for event {doc.event}'
        return tmpl.format(doc=self)


class EventDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(EventDocument, related_name='links')


class EventLink(LinkBase):
    event = models.ForeignKey(Event, related_name='links')


class EventSource(LinkBase):
    event = models.ForeignKey(Event, related_name='sources')


class EventParticipant(RelatedEntityBase):
    event = models.ForeignKey(Event, related_name='participants')
    note = models.TextField()

    def __str__(self):
        tmpl = '%s at %s'
        return tmpl % (self.name, self.event)


class EventAgendaItem(RelatedBase):
    description = models.TextField()
    order = models.CharField(max_length=100, blank=True)
    subjects = ArrayField(dbtype='text')
    notes = ArrayField(dbtype='text')
    event = models.ForeignKey(Event, related_name='agenda')


class EventRelatedEntity(RelatedEntityBase):
    agenda_item = models.ForeignKey(EventAgendaItem, related_name='related_entities')
    bill = models.ForeignKey(Bill, null=True)
    vote = models.ForeignKey(VoteEvent, null=True)
    note = models.TextField()

    @property
    def entity_name(self):
        if self.entity_type == 'vote' and self.vote_id:
            return self.vote.name
        elif self.entity_type == 'bill' and self.bill_id:
            return self.bill.name
        else:
            return super(EventRelatedEntity, self).entity_name

    @property
    def entity_id(self):
        if self.entity_type == 'vote':
            return self.vote_id
        if self.entity_type == 'bill':
            return self.bill_id
        return super(EventRelatedEntity, self).entity_id


class EventAgendaMedia(EventMediaBase):
    agenda_item = models.ForeignKey(EventAgendaItem, related_name='media')


class EventAgendaMediaLink(MimetypeLinkBase):
    media = models.ForeignKey(EventAgendaMedia, related_name='links')
