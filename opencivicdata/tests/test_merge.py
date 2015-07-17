from django.test import TestCase
from opencivicdata.models import merge
from opencivicdata.models import (Jurisdiction, LegislativeSession,                 # noqa
                                  Division, Organization,                           # noqa
                                  OrganizationIdentifier, OrganizationName,         # noqa
                                  OrganizationContactDetail, OrganizationSource,    # noqa
                                  Person, PersonIdentifier, PersonName,             # noqa
                                  PersonContactDetail, PersonLink, PersonSource,    # noqa
                                  Post, PostContactDetail, PostLink, Membership,    # noqa
                                  MembershipContactDetail, MembershipLink)          # noqa

class MergeTestCase(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name='Barack Obama',
                                            image='example.com',
                                            sort_name='Obama')
        self.organization1 = Organization.objects.create(name="House")
    def test_merge_of_different_classes(self):
        with self.assertRaises(AssertionError):
            merge.set_up_merge(self.person1, self.organization1, 'Person')
        self.assertEquals(Person.objects.count(), 1)
        self.assertEquals(Organization.objects.count(), 1)

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

    def test_membership_people_org_merge(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1)
        membership2 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1)
        membership1.merge(membership2)
        self.assertEqual(Membership.objects.count(), 1,
                         "Merge memberships with same person & org.")

    def test_membership_wrong_people(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1)
        membership2 = Membership.objects.create(person_id=self.pid2,
                                                organization_id=self.oid1)
        with self.assertRaises(AssertionError):
            membership1.merge(membership2)
        self.assertEqual(Membership.objects.count(), 2,
                         "Memberships w different people should not merge")
        membership1.merge(membership2, force=True)
        self.assertEqual(Membership.objects.count(), 1,
                         "Memberships w different people should merge if forced")
        self.assertEqual(Membership.objects.first().person_id, self.pid2,
                         "Force-merged memberships should retain person from newer membership")

    def test_membership_wrong_org(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1)
        membership2 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid2)
        with self.assertRaises(AssertionError):
            membership1.merge(membership2)
        self.assertEqual(Membership.objects.count(), 2,
                         "Memberships w different orgs should not merge")
        membership1.merge(membership2, force=True)
        self.assertEqual(Membership.objects.count(), 1,
                         "Memberships w different orgs should merge if forced")
        self.assertEqual(Membership.objects.first().organization_id, self.oid2,
                         "Force-merged memberships should retain org from newer membership")

    def test_memberships_subset_dates(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1,
                                                start_date='2014-01-01',
                                                end_date='2015-01-01')
        membership2 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1,
                                                start_date='2014-02-01',
                                                end_date='2014-03-01')
        membership1.merge(membership2)
        self.assertEqual(Membership.objects.count(), 1,
                         "Memberships w subsetted starts and ends should merge")
        self.assertEqual(Membership.objects.first().start_date, '2014-01-01',
                        "Resulting membership start date should be earliest")
        self.assertEqual(Membership.objects.first().end_date, '2015-01-01',
                        "Resulting membership end date should be latest")

    def test_memberships_overlapping_dates(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1,
                                                start_date='2014-01-01',
                                                end_date='2015-01-01')
        membership2 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1,
                                                start_date='2014-02-01',
                                                end_date='2015-03-01')
        membership1.merge(membership2)
        self.assertEqual(Membership.objects.count(), 1,
                         "Memberships w subsetted starts and ends should merge")
        self.assertEqual(Membership.objects.first().start_date, '2014-01-01',
                        "Resulting membership start date should be earliest")
        self.assertEqual(Membership.objects.first().end_date, '2015-03-01',
                        "Resulting membership end date should be latest")

    def test_memberships_nonoverlapping_dates(self):
        membership1 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1,
                                                start_date='2014-01-01',
                                                end_date='2014-02-01')
        membership2 = Membership.objects.create(person_id=self.pid1,
                                                organization_id=self.oid1,
                                                start_date='2014-03-01',
                                                end_date='2014-04-01')
        with self.assertRaises(AssertionError):
            membership1.merge(membership2)
        self.assertEqual(Membership.objects.count(), 2,
                         "Memberships w non-overlapping dates should not merge")
        membership1.merge(membership2, force=True)
        self.assertEqual(Membership.objects.count(), 1,
                         "Memberships w different non-overlapping dates should merge if forced")
        self.assertEqual(Membership.objects.first().start_date, '2014-01-01',
                         "Force-merged memberships should get earliest start date")
        self.assertEqual(Membership.objects.first().end_date, '2014-04-01',
                         "Force-merged memberships should get latest end date")

    def test_memberships_different_posts(self):
        post1 = Post.objects.create(label="post1", organization_id=self.oid1)
        post2 = Post.objects.create(label="post2", organization_id=self.oid1)
        mem1 = Membership.objects.create(post_id=post1.id,
                                         person_id=self.pid1,
                                         organization_id=self.oid1)
        mem2 = Membership.objects.create(post_id=post2.id,
                                         person_id=self.pid1,
                                         organization_id=self.oid1)
        with self.assertRaises(AssertionError):
            mem1.merge(mem2)

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


class OrgTestCase(TestCase):
    def setUp(self):
        self.org1 = Organization.objects.create(name="Org1",
                                                classification='legislature',
                                                founding_date='1776-07-04')
        self.org2 = Organization.objects.create(name="Org2",
                                                classification='government',
                                                dissolution_date='2012-12-21')
        d1 = Division.objects.create(id='ocd-division/country:us',
                                     name='America Online')
        j1 = Jurisdiction.objects.create(name="j1",
                                         url='example.com',
                                         division=d1,
                                         classification='committee',
                                         id='ocd-jurisdiction/country:us/committee')
        j2 = Jurisdiction.objects.create(name="j2",
                                         url='example.com',
                                         division=d1,
                                         id='ocd-jurisdiction/country:us/government')
        self.org3 = Organization.objects.create(name="Org3")
        self.org4 = Organization.objects.create(name="Org4",
                                                jurisdiction_id = j1.id)
        self.org5 = Organization.objects.create(name="Org5",
                                                jurisdiction_id = j1.id)
        self.org6 = Organization.objects.create(name="Org6",
                                                jurisdiction_id = j2.id)

    def test_merge_orgs_simple(self):
        org_id = self.org1.id
        self.org1.merge(self.org2)
        orgs = Organization.objects.all()
        self.assertEqual(len(orgs), 5, "Orgs should merge")
        new_org = Organization.objects.filter(name='Org2').first()
        self.assertEqual(new_org.id, org_id,
                         'Keep persistent org\'s id')
        self.assertEqual(new_org.classification, 'government',
                         'Keep newer org\'s classification')
        self.assertEqual(new_org.founding_date, '1776-07-04',
                         'Data trumps no-data')
        self.assertEqual(new_org.dissolution_date, '2012-12-21',
                         'Data trumps no-data')

    def test_merge_orgs_with_parents(self):
        self.org1.parent_id = self.org3.id
        self.org2.parent_id = self.org4.id
        self.org5.parent_id = self.org3.id
        self.org6.parent_id = self.org4.id
        self.org1.save()
        self.org2.save()
        self.org5.save()
        self.org6.save()
        self.org1.merge(self.org2)
        merged_org = Organization.objects.filter(name='Org2').first()
        two_org_parent = Organization.objects.filter(name='Org4').first()
        one_org_parent = Organization.objects.filter(name='Org3').first()
        self.assertEqual(Organization.objects.count(), 5,
                         'two orgs merged')
        self.assertEqual(merged_org.parent_id, self.org4.id,
                         'merged org gets newer org\'s parent')
        self.assertEqual(two_org_parent.children.count(), 2,
                         'merging doesn\'t impact other parent-child rlns')
        self.assertEqual(one_org_parent.children.count(), 1,
                         'merging removes obsolete org from parent')

    def test_org_merge_with_jurisdictions(self):
        with self.assertRaises(AssertionError):
            self.org4.merge(self.org6)
        self.assertEqual(Organization.objects.count(), 6,
                         'Orgs with different jurisdictions don\'t merge')
        self.org4.merge(self.org5)
        self.assertEqual(Organization.objects.count(), 5,
                         'Orgs w same jurisdiction merge')

class OrgWithParentsTestCase(TestCase):
    def setUp(self):
        self.org1 = Organization.objects.create(name="Org1")
        self.org2 = Organization.objects.create(name="Org2")
        self.org3 = Organization.objects.create(name="Org3",
                                                parent=self.org1)
        self.org4 = Organization.objects.create(name="Org4",
                                                parent=self.org2)

    def test_org_merge_with_parents(self):
        self.org1.merge(self.org2)
        org3 = Organization.objects.filter(name="Org3").first()
        org4 = Organization.objects.filter(name="Org4").first()
        self.assertEqual(org3.parent.name, "Org2")
        self.assertEqual(org4.parent.name, "Org2")
        self.assertEqual(Organization.objects.count(), 3)

class OrgMembershipTestCase(TestCase):
    def setUp(self):
        self.org1 = Organization.objects.create(name="Org1",
                                                classification='legislature',
                                                founding_date='1776-07-04')
        self.org2 = Organization.objects.create(name="Org2",
                                                classification='government',
                                                dissolution_date='2012-12-21')
        person1 = Person.objects.create(name="a")
        person2 = Person.objects.create(name="b")
        Membership.objects.create(person_id=person1.id, organization_id=self.org1.id)
        Membership.objects.create(person_id=person2.id, organization_id=self.org2.id)
        Membership.objects.create(person_id=person1.id, organization_id=self.org2.id)

    def test_merge_orgs_simple(self):
        self.org1.merge(self.org2)
        orgs = Organization.objects.all()
        self.assertEqual(len(orgs), 1, "Orgs should merge")
        new_org = orgs[0]
        self.assertEqual(len(new_org.memberships.all()), 2, "Memberships merge")        

class PersonBirthdayTestCase(TestCase):
  def setUp(self):
    self.p1 = Person.objects.create(name="George", birth_date='17760704')
    self.p2 = Person.objects.create(name="Thomas", birth_date='17760705')

  def test_birthday_mismatch(self):
      with self.assertRaises(AssertionError):
          self.p1.merge(self.p2)


class LockedFieldsTestCase(TestCase):
    def setUp(self):
        self.org1 = Organization.objects.create(name="Org1",
                                                image="org1.jpg",
                                                locked_fields=['image'])
        self.org2 = Organization.objects.create(name="Org2",
                                                image="org2.jpg",
                                                locked_fields=['founding_date'])  
    def test_org_merge_with_locked_fields(self):
        self.org1.merge(self.org2)
        self.assertEqual(Organization.objects.count(), 1,
                         'Orgs locked fields merge')
        merged_org = Organization.objects.first()
        self.assertEqual(merged_org.name, 'Org2',
                         'Keeps newer org\'s name')
        self.assertEqual(merged_org.image, 'org1.jpg',
                         'Keeps locked fields where relevant')
        self.assertEqual(merged_org.locked_fields, ['image', 'founding_date'],
                         'Keeps locked fields where relevant')