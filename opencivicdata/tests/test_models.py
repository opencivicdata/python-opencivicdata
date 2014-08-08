import pytest
from opencivicdata.models import (Jurisdiction, LegislativeSession, Division,
                                  Organization, OrganizationIdentifier, OrganizationName,
                                  OrganizationContactDetail, OrganizationSource,
                                  Person, PersonIdentifier, PersonName, PersonContactDetail,
                                  PersonLink, PersonSource, Post, PostContactDetail, PostLink,
                                  Membership, MembershipContactDetail, MembershipLink)
from django.core.exceptions import ValidationError


def test_division_subtypes_from_id():

    # simplest case
    assert Division.subtypes_from_id('ocd-division/country:us') == ({'country': 'us'}, 1)

    # ocd-divison part is optional
    assert Division.subtypes_from_id('country:us/state:ak/county:wild') == (
        {'country': 'us', 'subtype1': 'state', 'subid1': 'ak', 'subtype2': 'county',
         'subid2': 'wild'}, 3)

    # country is not optional
    with pytest.raises(ValueError):
        Division.subtypes_from_id('state:nc/city:raleigh')


@pytest.mark.django_db
def test_division_create():
    division_id = 'ocd-division/country:us/state:ak/county:wild'
    d = Division.objects.create(id=division_id, name='Wild County')
    assert d.country == 'us'
    assert d.subtype1 == 'state'
    assert d.subid1 == 'ak'
    assert d.subtype2 == 'county'
    assert d.subid2 == 'wild'
    assert division_id in str(d)


@pytest.mark.django_db
def test_division_children_of():
    us = Division.objects.create('ocd-division/country:us', name='US')
    ak = Division.objects.create('ocd-division/country:us/state:ak', name='Alaska')
    wild = Division.objects.create('ocd-division/country:us/state:ak/county:wild', name='Wild')
    mild = Division.objects.create('ocd-division/country:us/state:ak/county:mild', name='Mild')
    wild_a = Division.objects.create('ocd-division/country:us/state:ak/county:wild/place:a',
                                     name='A')
    wild_b = Division.objects.create('ocd-division/country:us/state:ak/county:wild/place:b',
                                     name='B')
    school = Division.objects.create('ocd-division/country:us/state:ak/county:wild/school:a',
                                     name='A')
    mild_a = Division.objects.create('ocd-division/country:us/state:ak/county:mild/place:a',
                                     name='A')
    mild_a = Division.objects.create('ocd-division/country:us/state:ak/county:mild/place:a/x:y',
                                     name='A')

    # simplest ==
    assert Division.objects.children_of('ocd-division/country:us')[0].id == ak.id

    # 3 divisions within wild county
    assert (Division.objects.children_of('ocd-division/country:us/state:ak/county:wild').count() ==
            3)

    # only one school in wild county
    assert Division.objects.children_of('ocd-division/country:us/state:ak/county:wild',
                                        subtype='school').count() == 1

    # 6 divisions beneath alaska up to 2 levels
    assert Division.objects.children_of('ocd-division/country:us/state:ak', depth=2).count() == 6

    # 7 divisions beneath alaska up to 3 levels
    assert Division.objects.children_of('ocd-division/country:us/state:ak', depth=3).count() == 7


@pytest.mark.django_db
def test_ocdid_default():
    o = Organization.objects.create(name='test org')
    assert o.id.startswith('ocd-organization/')
    assert o.pk == o.id
    p = Person.objects.create(name='test person')
    assert p.id.startswith('ocd-person/')


@pytest.mark.django_db
def test_ocdid_default_nondup():
    """ ensure that defaults actually vary """
    p1 = Person(name='test person 1')
    p2 = Person(name='test person 2')
    assert p1.id != p2.id


@pytest.mark.django_db
def test_ocdid_validation_jurisdiction():
    # this fails
    with pytest.raises(ValidationError):
        j = Jurisdiction(name='test juris', id='ocd-division/country:us/test:something/else',
                         url='http://example.com')
        j.full_clean(exclude=['division'])

    # this succeeds
    j = Jurisdiction(name='test juris', id='ocd-jurisdiction/country:us/test:something/else',
                     url='http://example.com')
    j.full_clean(exclude=['division'])


@pytest.mark.django_db
def test_ocdid_validation_other():
    # this test should handle everything that isn't a jurisdiction

    # this succeeds
    o = Organization(name='test org')
    o.full_clean(exclude=['parent', 'jurisdiction'])

    # this raises
    with pytest.raises(ValidationError):
        o = Organization(name='this is a test', id='ocd-organization/3')
        o.full_clean(exclude=['parent', 'jurisdiction'])
