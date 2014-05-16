import uuid
from django.db import models
from django.core.validators import RegexValidator
from jsonfield import JSONField
from uuidfield import UUIDField
from .. import common


class OCDIDField(models.CharField):

    def __init__(self, *args, **kwargs):
        self.ocd_type = kwargs.pop('ocd_type')
        if self.ocd_type != 'jurisdiction':
            kwargs['default'] = lambda: 'ocd-{}/{}'.format(self.ocd_type, uuid.uuid4())
            # len('ocd-') + len(ocd_type) + len('/') + len(uuid)
            #       = 4 + len(ocd_type) + 1 + 36
            #       = len(ocd_type) + 41
            kwargs['max_length'] = 41 + len(self.ocd_type)
            regex = '^ocd-' + self.ocd_type  + '/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$'
        else:
            kwargs['max_length'] = 300
            regex = common.JURISDICTION_ID_REGEX

        kwargs['primary_key'] = True
        # get pattern property if it exists, otherwise just return the object (hopefully a string)
        msg = 'ID must match ' + getattr(regex, 'pattern', regex)
        kwargs['validators'] = [RegexValidator(regex=regex, message=msg)]
        super(OCDIDField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(OCDIDField, self).deconstruct()
        if self.ocd_type != 'jurisdiction':
            kwargs.pop('default')
        kwargs.pop('max_length')
        kwargs.pop('primary_key')
        kwargs['ocd_type'] = self.ocd_type



class OCDBase(models.Model):
    """ common base fields across all top-level models """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extras = JSONField(default='{}', blank=True)

    class Meta:
        abstract = True


class RelatedBase(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    class Meta:
        abstract = True


class ContactDetailBase(RelatedBase):
    type = models.CharField(max_length=50, choices=common.CONTACT_TYPE_CHOICES)
    value = models.CharField(max_length=300, blank=True)
    note = models.CharField(max_length=300, blank=True)
    label = models.CharField(max_length=300, blank=True)

    class Meta:
        abstract = True


class IdentifierBase(RelatedBase):
    identifier = models.CharField(max_length=300)
    scheme = models.CharField(max_length=300)

    class Meta:
        abstract = True


class OtherNameBase(RelatedBase):
    name = models.CharField(max_length=500)
    note = models.CharField(max_length=500, blank=True)
    start_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10)      # YYYY[-MM[-DD]]

    class Meta:
        abstract = True


class LinkBase(RelatedBase):
    note = models.CharField(max_length=300, blank=True)
    url = models.URLField()

    class Meta:
        abstract = True
