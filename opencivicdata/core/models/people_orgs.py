from __future__ import unicode_literals
import datetime
from django.db import models
from django.db.models import Q, QuerySet
from django.utils.encoding import python_2_unicode_compatible
from .base import OCDBase, LinkBase, OCDIDField, RelatedBase, IdentifierBase
from .division import Division
from .jurisdiction import Jurisdiction
from ... import common

# abstract models


@python_2_unicode_compatible
class ContactDetailBase(RelatedBase):
    type = models.CharField(max_length=50, choices=common.CONTACT_TYPE_CHOICES)
    value = models.CharField(max_length=300)
    note = models.CharField(max_length=300, blank=True)
    label = models.CharField(max_length=300, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}: {}'.format(self.get_type_display(), self.value)


@python_2_unicode_compatible
class OtherNameBase(RelatedBase):
    name = models.CharField(max_length=500, db_index=True)
    note = models.CharField(max_length=500, blank=True)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)      # YYYY[-MM[-DD]]

    class Meta:
        abstract = True

    def __str__(self):
        return '{} ({})'.format(self.name, self.note)


# the actual models

@python_2_unicode_compatible
class Organization(OCDBase):
    id = OCDIDField(ocd_type='organization')
    name = models.CharField(max_length=300)
    image = models.URLField(blank=True, max_length=2000)
    parent = models.ForeignKey('self', related_name='children', null=True)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='organizations', null=True)
    classification = models.CharField(max_length=100, blank=True,
                                      choices=common.ORGANIZATION_CLASSIFICATION_CHOICES)
    founding_date = models.CharField(max_length=10, blank=True)     # YYYY[-MM[-DD]]
    dissolution_date = models.CharField(max_length=10, blank=True)  # YYYY[-MM[-DD]]

    def __str__(self):
        return self.name

    # Access all "ancestor" organizations
    def get_parents(self):
        org = self
        while True:
            org = org.parent
            # Django accesses parents lazily, so have to check if one actually exists
            if org:
                yield org
            else:
                break

    def get_current_members(self):
        """ return all Person objects w/ current memberships to org """
        today = datetime.date.today().isoformat()

        return Person.objects.filter(Q(memberships__start_date='') |
                                     Q(memberships__start_date__lte=today),
                                     Q(memberships__end_date='') |
                                     Q(memberships__end_date__gte=today),
                                     memberships__organization_id=self.id
                                     )

    class Meta:
        db_table = 'opencivicdata_organization'
        index_together = [
            ['jurisdiction', 'classification', 'name'],
            ['classification', 'name'],
        ]


@python_2_unicode_compatible
class OrganizationIdentifier(IdentifierBase):
    organization = models.ForeignKey(Organization, related_name='identifiers')

    def __str__(self):
        tmpl = '%s identifies %s'
        return tmpl % (self.identifier, self.organization)

    class Meta:
        db_table = 'opencivicdata_organizationidentifier'


class OrganizationName(OtherNameBase):
    organization = models.ForeignKey(Organization, related_name='other_names')

    class Meta:
        db_table = 'opencivicdata_organizationname'


class OrganizationContactDetail(ContactDetailBase):
    organization = models.ForeignKey(Organization, related_name='contact_details')

    class Meta:
        db_table = 'opencivicdata_organizationcontactdetail'


class OrganizationLink(LinkBase):
    organization = models.ForeignKey(Organization, related_name='links')

    class Meta:
        db_table = 'opencivicdata_organizationlink'


class OrganizationSource(LinkBase):
    organization = models.ForeignKey(Organization, related_name='sources')

    class Meta:
        db_table = 'opencivicdata_organizationsource'


@python_2_unicode_compatible
class Post(OCDBase):
    id = OCDIDField(ocd_type='post')
    label = models.CharField(max_length=300)
    role = models.CharField(max_length=300, blank=True)
    organization = models.ForeignKey(Organization, related_name='posts')
    division = models.ForeignKey(Division, related_name='posts', null=True, blank=True,
                                 default=None)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    maximum_memberships = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'opencivicdata_post'
        index_together = [
            ['organization', 'label']
        ]

    def __str__(self):
        return '{} - {} - {}'.format(self.role, self.label, self.organization)


class PostContactDetail(ContactDetailBase):
    post = models.ForeignKey(Post, related_name='contact_details')

    class Meta:
        db_table = 'opencivicdata_postcontactdetail'


class PostLink(LinkBase):
    post = models.ForeignKey(Post, related_name='links')

    class Meta:
        db_table = 'opencivicdata_postlink'


class PersonQuerySet(QuerySet):
    def member_of(self, organization_name, current_only=True):
        filter_params = []

        if current_only:
            today = datetime.date.today().isoformat()

            filter_params = [Q(memberships__start_date='') |
                             Q(memberships__start_date__lte=today),
                             Q(memberships__end_date='') |
                             Q(memberships__end_date__gte=today),
                             ]
        if organization_name.startswith('ocd-organization/'):
            qs = self.filter(*filter_params,
                             memberships__organization_id=organization_name)
        else:
            qs = self.filter(*filter_params,
                             memberships__organization__name=organization_name)
        return qs


@python_2_unicode_compatible
class Person(OCDBase):
    objects = PersonQuerySet.as_manager()

    id = OCDIDField(ocd_type='person')
    name = models.CharField(max_length=300, db_index=True)
    sort_name = models.CharField(max_length=100, default='', blank=True)
    family_name = models.CharField(max_length=100, blank=True)
    given_name = models.CharField(max_length=100, blank=True)

    image = models.URLField(blank=True, max_length=2000)
    gender = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=500, blank=True)
    national_identity = models.CharField(max_length=300, blank=True)
    biography = models.TextField(blank=True)
    birth_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    death_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]

    def __str__(self):
        return self.name

    def add_other_name(self, name, note=""):
        PersonName.objects.create(name=name, note=note, person_id=self.id)

    class Meta:
        db_table = 'opencivicdata_person'
        verbose_name_plural = "people"


class PersonIdentifier(IdentifierBase):
    person = models.ForeignKey(Person, related_name='identifiers')

    class Meta:
        db_table = 'opencivicdata_personidentifier'


class PersonName(OtherNameBase):
    person = models.ForeignKey(Person, related_name='other_names')

    class Meta:
        db_table = 'opencivicdata_personname'


class PersonContactDetail(ContactDetailBase):
    person = models.ForeignKey(Person, related_name='contact_details')

    class Meta:
        db_table = 'opencivicdata_personcontactdetail'


class PersonLink(LinkBase):
    person = models.ForeignKey(Person, related_name='links')

    class Meta:
        db_table = 'opencivicdata_personlink'


class PersonSource(LinkBase):
    person = models.ForeignKey(Person, related_name='sources')

    class Meta:
        db_table = 'opencivicdata_personsource'


@python_2_unicode_compatible
class Membership(OCDBase):
    id = OCDIDField(ocd_type='membership')
    organization = models.ForeignKey(Organization, related_name='memberships')
    person = models.ForeignKey(Person, related_name='memberships', null=True)
    person_name = models.CharField(max_length=300, blank=True, default='')
    post = models.ForeignKey(Post, related_name='memberships', null=True)
    on_behalf_of = models.ForeignKey(Organization, related_name='memberships_on_behalf_of',
                                     null=True)
    label = models.CharField(max_length=300, blank=True)
    role = models.CharField(max_length=300, blank=True)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)      # YYYY[-MM[-DD]]

    class Meta:
        db_table = 'opencivicdata_membership'
        index_together = [
            ['organization', 'person', 'label', 'post']
        ]

    def __str__(self):
        return '{} in {} ({})'.format(self.person, self.organization, self.role)


class MembershipContactDetail(ContactDetailBase):
    membership = models.ForeignKey(Membership, related_name='contact_details')

    class Meta:
        db_table = 'opencivicdata_membershipcontactdetail'


class MembershipLink(LinkBase):
    membership = models.ForeignKey(Membership, related_name='links')

    class Meta:
        db_table = 'opencivicdata_membershiplink'
