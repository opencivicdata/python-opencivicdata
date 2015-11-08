from django.test import TestCase
from opencivicdata.models import (Division, Organization,
                                  OrganizationIdentifier, OrganizationName,
                                  OrganizationContactDetail, OrganizationSource,
                                  Person, PersonIdentifier, PersonName,
                                  PersonContactDetail, PersonLink, PersonSource,
                                  Post, PostContactDetail, PostLink, Membership,
                                  MembershipContactDetail, MembershipLink)


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
        self.person1.merge(self.person2)
        obama_set = Person.objects.filter(name='Barack Obama')
        obama = obama_set.first()
        self.assertEqual(len(obama_set), 1,
                         "There should only be one person after merge.")
        self.assertEqual(obama.sort_name, 'Obama',
                         "Sort name should match most recently updated.")
        self.assertEqual(obama.gender, 'M',
                         "Data should trump empty, no matter the update order.")


    def test_merge_with_contact_details(self):
        self.person1.merge(self.person2)
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
        self.person1.merge(self.person2)
        obama = Person.objects.filter(name='Barack Obama').first()
        self.assertEqual(len(obama.identifiers.all()), 3,
                         "New person object retains all non-duplicate identifiers")
        self.assertEqual(len(obama.identifiers.filter(identifier='4567')), 2,
                         "Identifiers w same ID but different schema not overwritten")
        self.assertEqual(len(obama.identifiers.filter(identifier='1234')), 1,
                         "If identifiers have same identifier&scheme, only one is kept")

    def test_merge_with_links(self):
        self.person1.merge(self.person2)
        obama = Person.objects.filter(name='Barack Obama').first()
        self.assertEqual(len(obama.links.all()), 1,
                         "New person object retains all non-duplicate identifiers")
        self.assertEqual(obama.links.first().note, 'official',
                         "Link attached to newer person retained when conflict")

    def test_merge_with_memberships(self):
        org1 = Organization.objects.create(name="Org1")
        org2 = Organization.objects.create(name="Org2")
        org3 = Organization.objects.create(name="Org3")
        org4 = Organization.objects.create(name="Org4")
        org5 = Organization.objects.create(name="Org5")

        #these two should merge:

        Membership.objects.create(person_id=self.person1.id,
                                  organization_id=org1.id)
        Membership.objects.create(person_id=self.person2.id,
                                  organization_id=org1.id)

        #these two should merge, and have start/end dates
        Membership.objects.create(person_id=self.person1.id,
                                  organization_id=org2.id)
        Membership.objects.create(person_id=self.person2.id,
                                  organization_id=org2.id,
                                  start_date='2015-01-02',
                                  end_date='2016-01-02')

        #these two should merge
        Membership.objects.create(person_id=self.person1.id,
                                  organization_id=org3.id,
                                  start_date='2015-02-03',
                                  end_date='2015-03-03')
        Membership.objects.create(person_id=self.person2.id,
                                  organization_id=org3.id,
                                  start_date='2015-01-03',
                                  end_date='2016-01-03')

        #these two should merge
        Membership.objects.create(person_id=self.person1.id,
                                  organization_id=org4.id,
                                  start_date='2015-01-04',
                                  end_date='2015-03-04')
        Membership.objects.create(person_id=self.person2.id,
                                  organization_id=org4.id,
                                  start_date='2015-02-15',
                                  end_date='2016-03-04')
        #these two should not merge
        Membership.objects.create(person_id=self.person1.id,
                                  organization_id=org5.id,
                                  start_date='2015-02-05',
                                  end_date='2015-03-05')
        Membership.objects.create(person_id=self.person2.id,
                                  organization_id=org5.id,
                                  start_date='2015-04-15',
                                  end_date='2016-03-05')

        self.person1.merge(self.person2)

        obama = Person.objects.filter(name='Barack Obama').first()
        self.assertEqual(obama.memberships.count(), 6,
                         "right number of merges need to happen.")

        org2_mem = obama.memberships.filter(organization_id=org2.id).first()
        self.assertEqual(org2_mem.start_date,'2015-01-02',
                         "start date for org2 memberships is earliest")
        self.assertEqual(org2_mem.end_date,'2016-01-02',
                         "end date for org2 memberships is latest")

        org3_mem = obama.memberships.filter(organization_id=org3.id).first()
        self.assertEqual(org3_mem.start_date,'2015-01-03',
                         "start date for org3 memberships is earliest")
        self.assertEqual(org3_mem.end_date,'2016-01-03',
                         "end date for org3 memberships is latest")

        org4_mem = obama.memberships.filter(organization_id=org4.id).first()
        self.assertEqual(org4_mem.start_date,'2015-01-04',
                         "start date for org4 memberships is latest")
        self.assertEqual(org4_mem.end_date,'2016-03-04',
                         "end date for org4 memberships is latest")

        org5_mems = obama.memberships.filter(organization_id=org5.id)
        self.assertEqual(len(org5_mems), 2,
                         "org5 memberships don't merge")


class PersonBirthdayTestCase(TestCase):
  def setUp(self):
    self.p1 = Person.objects.create(name="George", birth_date='17760704')
    self.p2 = Person.objects.create(name="Thomas", birth_date='17760705')

  def test_birthday_mismatch(self):
      with self.assertRaises(AssertionError):
          self.p1.merge(self.p2)
