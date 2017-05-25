from django.test import TestCase
from opencivicdata.core.models import (Division, Organization, Person,
                                       Jurisdiction, Post, Membership)
from opencivicdata.legislative.models import Bill, BillSponsorship
from opencivicdata.merge import merge

# TODO: compute_diff test?


class TestPersonMerge(TestCase):

    def test_simple_merge(self):
        # create person2 first but ensure it's created_at gets carried over
        person2 = Person.objects.create(name='Barack Obama',
                                        sort_name='Obama',
                                        gender='Male')
        person1 = Person.objects.create(name='Barack Obama',
                                        sort_name='Barack')
        p2_id = person2.id
        p2_created = person2.created_at

        merge(person1, person2)
        self.assertEqual(Person.objects.count(), 1,
                         "There should only be one person after merge.")
        obama = Person.objects.get()
        # add identifier
        self.assertEqual(obama.identifiers.get().identifier, p2_id)
        # don't add other name if they match
        self.assertEqual(obama.other_names.count(), 0)
        self.assertEqual(obama.sort_name, 'Barack',
                         "Simple fields should take obj1's properties")
        self.assertEqual(obama.created_at, p2_created)
        self.assertGreater(obama.updated_at, obama.created_at)
        self.assertEqual(obama.gender, 'Male',
                         "Data should trump empty, no matter the update order.")
        assert set(obama.locked_fields) == {'identifiers', 'gender', 'sort_name'}

    def test_other_name_merge(self):
        person1 = Person.objects.create(name='Barack Obama')
        person2 = Person.objects.create(name='Barry Obama')

        merge(person1, person2)

        # moved name into other_names
        assert person1.other_names.get().name == 'Barry Obama'

        # check locked_fields
        obama = Person.objects.get()
        assert set(obama.locked_fields) == {'identifiers', 'name', 'other_names'}

    def test_no_self_merge(self):
        person1 = Person.objects.create(name='Barack Obama')

        with self.assertRaises(ValueError):
            merge(person1, person1)

    def test_merge_contact_details(self):
        person1 = Person.objects.create(name='Barack Obama')
        person2 = Person.objects.create(name='Barack Obama')
        person1.contact_details.create(type='fax', value='555-123-4567')
        person2.contact_details.create(type='fax', value='555-123-4567',
                                       note="Throw out your fax!")
        person1.contact_details.create(type='email', value='obama@aol.com')
        person2.contact_details.create(type='email', value='prez@america.gov')

        merge(person1, person2)
        obama = Person.objects.get()
        # no deduping for now
        self.assertEqual(obama.contact_details.count(), 4)
        assert set(obama.locked_fields) == {'identifiers', 'contact_details'}

    def test_merge_related_obj(self):
        person1 = Person.objects.create(name='Barack Obama')
        person2 = Person.objects.create(name='Barack Obama')
        d = Division.objects.create(id='ocd-division/country:us', name='US')
        j = Jurisdiction.objects.create(name='US', division=d)
        l = j.legislative_sessions.create(name='2015')
        b = Bill.objects.create(identifier='HB 1', legislative_session=l)
        sp = BillSponsorship.objects.create(bill=b, person=person2)

        merge(person1, person2)

        sp = BillSponsorship.objects.get()
        assert sp.person == person1
        person = Person.objects.get()
        assert set(person.locked_fields) == {'identifiers'}

    def test_merge_memberships(self):
        person1 = Person.objects.create(name='Barack Obama')
        person2 = Person.objects.create(name='Barack Obama')
        d = Division.objects.create(id='ocd-division/country:us', name='US')
        j = Jurisdiction.objects.create(name='US', division=d)
        dem = Organization.objects.create(name='Democratic', classification='party')
        gov = Organization.objects.create(name='Federal Government',
                                          jurisdiction=j,
                                          classification='government')
        # this isn't how you'd really use posts
        pres = Post.objects.create(label='President', organization=gov)
        sen = Post.objects.create(label='Senator', organization=gov)
        Membership.objects.create(organization=dem, person=person1)
        Membership.objects.create(organization=gov, person=person1, post=pres)
        Membership.objects.create(organization=dem, person=person2)
        Membership.objects.create(organization=gov, person=person1, post=sen)

        merge(person1, person2)
        person = Person.objects.get()
        # ensure that the party memberships are deduped and others are kept
        assert person.memberships.count() == 3
        assert pres.memberships.count() == 1
        assert sen.memberships.count() == 1
        assert set(person.locked_fields) == {'memberships', 'identifiers'}
