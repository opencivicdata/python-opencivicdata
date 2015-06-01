from django.test import TestCase
from opencivicdata.admin import merge
from opencivicdata.models import (Jurisdiction, LegislativeSession,                 # noqa
                                  Division, Organization,                           # noqa
                                  OrganizationIdentifier, OrganizationName,         # noqa
                                  OrganizationContactDetail, OrganizationSource,    # noqa
                                  Person, PersonIdentifier, PersonName,             # noqa
                                  PersonContactDetail, PersonLink, PersonSource,    # noqa
                                  Post, PostContactDetail, PostLink, Membership,    # noqa
                                  MembershipContactDetail, MembershipLink)          # noqa

class MembershipTestCase(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name='Barack Obama',
                                            image='example.com',
                                            sort_name='Obama')
        self.person2 = Person.objects.create(name='Michelle Obama',
                                            image='example.com',
                                            sort_name='Obama')
        self.pid1 = self.person1.id
        self.pid2 = self.person2.id

        self.organization1 = Organization.objects.create(name="House")
        self.organization2 = Organization.objects.create(name="Senate")

        self.oid1 = self.organization1.id
        self.oid2 = self.organization2.id

    def test_membership_people_merge(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1)
        membership2 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1)
        merge.merge_memberships(membership1, membership2)
        self.assertEqual(Membership.objects.count(), 1,
                         "Merge memberships with same person & org.")



class PersonTestCase(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name='Barack Obama',
                                        image='example.com',
                                        sort_name='Barack',
                                        gender='M')

        self.person2 = Person.objects.create(name='Barack Obama',
                                        image='example.com',
                                        sort_name='Obama')

        id1 = self.person1.id
        id2 = self.person2.id

        PersonContactDetail.objects.create(type='fax',
                                           value='555-123-4567',
                                           person_id=id1)
        PersonContactDetail.objects.create(type='fax',
                                           value='555-123-4567',
                                           note="Throw out your fax!",
                                           person_id=id2)
        PersonContactDetail.objects.create(type='email',
                                           value='prez@america.gov',
                                           person_id=id2)
        PersonContactDetail.objects.create(type='email',
                                           value='obama@aol.com',
                                           person_id=id1)

        PersonIdentifier.objects.create(scheme='openstates',
                                        identifier='1234',
                                        person_id=id1)
        PersonIdentifier.objects.create(scheme='openstates',
                                        identifier='1234',
                                        person_id=id2)
        PersonIdentifier.objects.create(scheme='openstates',
                                        identifier='4567',
                                        person_id=id1)
        PersonIdentifier.objects.create(scheme='another_source',
                                        identifier='4567',
                                        person_id=id2)

        PersonLink.objects.create(url='whitehouse.gov',
                                  note='official',
                                  person_id=id2)
        PersonLink.objects.create(url='whitehouse.gov',
                                  note='whitehouse',
                                  person_id=id1)

    def test_simple_merge(self):
        merge.merge_people(self.person1, self.person2)
        obama_set = Person.objects.filter(name='Barack Obama')
        obama = obama_set.first()
        self.assertEqual(len(obama_set), 1,
                         "There should only be one person after merge.")
        self.assertEqual(obama.sort_name, 'Obama',
                         "Sort name should match most recently updated.")
        self.assertEqual(obama.gender, 'M',
                         "Data should trump empty, no matter the update order.")


    def test_merge_with_contact_details(self):
        merge.merge_people(self.person1, self.person2)
        obama = Person.objects.filter(name='Barack Obama').first()
        self.assertEqual(len(obama.contact_details.all()),3,
                         "New person retains all non-duplicate contact details")
        self.assertEqual(len(obama.contact_details.filter(type="fax")), 1,
                         "Contact details with same value and type merged")
        self.assertEqual(len(obama.contact_details.filter(type="email")), 2,
                         "Contact details of same type not merged if val differs")
        self.assertEqual(obama.contact_details.filter(type="fax").first().note,
                         "Throw out your fax!",
                         "Newer person's contact detail retained when conflict")

    def test_merge_with_identifiers(self):
        merge.merge_people(self.person1, self.person2)
        obama = Person.objects.filter(name='Barack Obama').first()
        self.assertEqual(len(obama.identifiers.all()), 3,
                         "New person object retains all non-duplicate identifiers")
        self.assertEqual(len(obama.identifiers.filter(identifier='4567')), 2,
                         "Identifiers w same ID but different schema not overwritten")
        self.assertEqual(len(obama.identifiers.filter(identifier='1234')), 1,
                         "If identifiers have same identifier&scheme, only one is kept")

    def test_merge_with_links(self):
        merge.merge_people(self.person1, self.person2)
        obama = Person.objects.filter(name='Barack Obama').first()
        self.assertEqual(len(obama.links.all()), 1,
                         "New person object retains all non-duplicate identifiers")
        self.assertEqual(obama.links.first().note, 'official',
                         "Link attached to newer person retained when conflict")
