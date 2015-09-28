import datetime
from django.db import models, transaction
from django.db.models import Q
from .base import OCDBase, LinkBase, OCDIDField, RelatedBase, IdentifierBase
from .division import Division
from .jurisdiction import Jurisdiction
from .. import common
from .merge import start_and_end_dates, common_merge, set_up_merge
#from .merge import common_merge, start_and_end_dates

# abstract models


class ContactDetailBase(RelatedBase):
    type = models.CharField(max_length=50, choices=common.CONTACT_TYPE_CHOICES)
    value = models.CharField(max_length=300)
    note = models.CharField(max_length=300, blank=True)
    label = models.CharField(max_length=300, blank=True)

    def transfer_contact_details(persistent, obsolete):
        for contact in obsolete.contact_details.all():
            matches = persistent.contact_details.filter(type=contact.type,
                                                                   value=contact.value)
            for m in matches:
                #get rid of old contact details that match a new one
                m.delete()

            persistent.contact_details.add(contact)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}: {}'.format(self.get_type_display(), self.value)


class OtherNameBase(RelatedBase):
    name = models.CharField(max_length=500, db_index=True)
    note = models.CharField(max_length=500, blank=True)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)      # YYYY[-MM[-DD]]

    class Meta:
        abstract = True

# the actual models

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

    @transaction.atomic
    def merge(self, obsolete_obj, force=False):
        persistent_obj = self
        new, old = set_up_merge(persistent_obj, obsolete_obj, 'Organization')

        #don't merge if they have different jurisdictions
        if (old.jurisdiction_id != ''
                and new.jurisdiction_id != ''
                and old.jurisdiction_id != new.jurisdiction_id
                and not force):
            raise AssertionError("Refusing to merge orgs from different jurisdictions.")

        valid_jurisdiction = new.jurisdiction or old.jurisdiction
        setattr(persistent_obj, "jurisdiction", valid_jurisdiction)


        ContactDetailBase.transfer_contact_details(persistent_obj, obsolete_obj)
        IdentifierBase.transfer_identifiers(persistent_obj, obsolete_obj)
        LinkBase.transfer_links(persistent_obj, obsolete_obj, "links")
        LinkBase.transfer_links(persistent_obj, obsolete_obj, "sources")

        # memberships
        # if a membership with the same post and org exists in old:
        for new_mem in new.memberships.all():
            filter_keys = {'person': new_mem.person,
                           'post': new_mem.post}
            for old_mem in old.memberships.filter(**filter_keys):
                # if they don't overlap, keep them both

                if (new_mem.end_date and old_mem.end_date
                        and new_mem.end_date < old_mem.start_date):
                    # the memberships don't overlap, don't merge
                    pass
                elif (old_mem.end_date and new_mem.start_date
                        and old_mem.end_date < new_mem.start_date):
                    # the memberships don't overlap, don't merge
                    pass
                else:
                    new_mem.organization = persistent_obj
                    old_mem.merge(new_mem)

        #transfer all orgs that have obselete as a parent
        for child in obsolete_obj.children.all():
            child.parent = persistent_obj
            child.save()


        common_merge(persistent_obj, obsolete_obj, new, old, ['name',
                     'image', 'classification', 'extras',
                     'founding_date', 'dissolution_date', 'parent_id'],
                     [], ['jurisdiction_id'], False)

    class Meta:
        index_together = [
            ['jurisdiction', 'classification', 'name'],
            ['classification', 'name'],
        ]


class OrganizationIdentifier(IdentifierBase):
    organization = models.ForeignKey(Organization, related_name='identifiers')

    def __str__(self):
        tmpl = '%s identifies %s'
        return tmpl % (self.identifier, self.organization)


class OrganizationName(OtherNameBase):
    organization = models.ForeignKey(Organization, related_name='other_names')


class OrganizationContactDetail(ContactDetailBase):
    organization = models.ForeignKey(Organization, related_name='contact_details')


class OrganizationLink(LinkBase):
    organization = models.ForeignKey(Organization, related_name='links')


class OrganizationSource(LinkBase):
    organization = models.ForeignKey(Organization, related_name='sources')


class Post(OCDBase):
    id = OCDIDField(ocd_type='post')
    label = models.CharField(max_length=300)
    role = models.CharField(max_length=300, blank=True)
    organization = models.ForeignKey(Organization, related_name='posts')
    division = models.ForeignKey(Division, related_name='posts', null=True, blank=True,
                                 default=None)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]

    class Meta:
        index_together = [
            ['organization', 'label']
        ]

    def __str__(self):
        return '{} - {} - {}'.format(self.role, self.label, self.organization)


class PostContactDetail(ContactDetailBase):
    post = models.ForeignKey(Post, related_name='contact_details')


class PostLink(LinkBase):
    post = models.ForeignKey(Post, related_name='links')


class Person(OCDBase):
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
        PersonName.objects.create(name=name,
                        note=note,
                        person_id=self.id)

    class Meta:
        verbose_name_plural = "people"

    @transaction.atomic
    def merge(self, obsolete_obj, force=False):
        persistent_obj = self
        new, old = set_up_merge(persistent_obj, obsolete_obj, 'Person')

        if (old.birth_date != ''
                and new.birth_date != ''
                and old.birth_date != new.birth_date
                and not force):
            raise AssertionError("Refusing to merge people with different birthdays.")

        valid_birthdate = new.birth_date or old.birth_date
        setattr(persistent_obj, "birth_date", valid_birthdate)

        if persistent_obj.name not in persistent_obj.other_names.all():
            persistent_obj.add_other_name(persistent_obj.name)
        if obsolete_obj.name not in persistent_obj.other_names.all():
            persistent_obj.add_other_name(obsolete_obj.name)

        for n in obsolete_obj.other_names.all():
            persistent_obj.other_names.add(n)

        ContactDetailBase.transfer_contact_details(persistent_obj, obsolete_obj)
        IdentifierBase.transfer_identifiers(persistent_obj, obsolete_obj)
        LinkBase.transfer_links(persistent_obj, obsolete_obj, "links")
        LinkBase.transfer_links(persistent_obj, obsolete_obj, "sources")

        # memberships
        # if a membership with the same post and org exists in old:
        for new_mem in new.memberships.all():
            filter_keys = {'organization': new_mem.organization,
                           'post': new_mem.post}
            for old_mem in old.memberships.filter(**filter_keys):
                # if they don't overlap, keep them both

                if (new_mem.end_date and old_mem.end_date
                        and new_mem.end_date < old_mem.start_date):
                    # the memberships don't overlap, don't merge
                    pass
                elif (old_mem.end_date and new_mem.start_date
                        and old_mem.end_date < new_mem.start_date):
                    # the memberships don't overlap, don't merge
                    pass
                else:
                    new_mem.person = persistent_obj
                    old_mem.merge(new_mem)


        common_merge(persistent_obj, obsolete_obj, new, old, ['sort_name', 'family_name',
                     'given_name', 'image', 'gender', 'summary',
                     'national_identity', 'biography',
                     'death_date', 'extras'], [],
                    ['birth_date', 'name'], False)


class PersonIdentifier(IdentifierBase):
    person = models.ForeignKey(Person, related_name='identifiers')


class PersonName(OtherNameBase):
    person = models.ForeignKey(Person, related_name='other_names')


class PersonContactDetail(ContactDetailBase):
    person = models.ForeignKey(Person, related_name='contact_details')


class PersonLink(LinkBase):
    person = models.ForeignKey(Person, related_name='links')


class PersonSource(LinkBase):
    person = models.ForeignKey(Person, related_name='sources')


class Membership(OCDBase):
    id = OCDIDField(ocd_type='membership')
    organization = models.ForeignKey(Organization, related_name='memberships')
    person = models.ForeignKey(Person, related_name='memberships')
    post = models.ForeignKey(Post, related_name='memberships', null=True)
    on_behalf_of = models.ForeignKey(Organization, related_name='memberships_on_behalf_of',
                                     null=True)
    label = models.CharField(max_length=300, blank=True)
    role = models.CharField(max_length=300, blank=True)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)      # YYYY[-MM[-DD]]

    class Meta:
        index_together = [
            ['organization', 'person', 'label', 'post']
        ]

    def __str__(self):
        return '{} in {} ({})'.format(self.person, self.organization, self.role)

    @transaction.atomic
    def merge(self, obsolete_obj, force=False):
        #current obj persists, keeping newer fields when they conflict
        persistent_obj = self
        new, old = set_up_merge(persistent_obj, obsolete_obj, 'Membership')
        if force == False:

            if (new.post and old.post and new.post != old.post):
                msg = "Memberships have different posts. Refusing to merge "\
                      "without forcing. This is probably a bad idea. "\
                      "Consider yourself warned."
                raise AssertionError(msg)

            if (new.person and old.person and new.person != old.person and not force):
                msg = "Memberships have different people. Refusing to merge "\
                      "without forcing. This is probably a bad idea. "\
                      "Consider yourself warned."
                raise AssertionError(msg)

            if (new.organization and old.organization
                and new.organization != old.organization and not force):
                    msg = "Memberships have different organizations. Refusing "\
                          "to merge without forcing. This is probably a bad idea. "\
                          "Consider yourself warned."
                    raise AssertionError(msg)

        # TODO check for human edited fields

        keep_old, keep_new, custom_fields = start_and_end_dates(persistent_obj,
                                                                obsolete_obj,
                                                                force=force,
                                                                keep_old=[],
                                                                keep_new=[],
                                                                custom_fields=[])
        keep_new.extend(['organization_id', 'person_id', 'post_id', 'on_behalf_of_id',
                        'label', 'role'])

        ContactDetailBase.transfer_contact_details(old, new)
        LinkBase.transfer_links(old, new, "links")

        keep_new.append('extras')

        common_merge(persistent_obj, obsolete_obj, new, old,
                     keep_new, keep_old, custom_fields, False)


class MembershipContactDetail(ContactDetailBase):
    membership = models.ForeignKey(Membership, related_name='contact_details')


class MembershipLink(LinkBase):
    membership = models.ForeignKey(Membership, related_name='links')
