import pytest
from django.contrib.gis.geos import Point
from opencivicdata.models import (Jurisdiction, LegislativeSession,                 # noqa
                                  Division, Organization,                           # noqa
                                  OrganizationIdentifier, OrganizationName,         # noqa
                                  OrganizationContactDetail, OrganizationSource,    # noqa
                                  Person, PersonIdentifier, PersonName,             # noqa
                                  PersonContactDetail, PersonLink, PersonSource,    # noqa
                                  Post, PostContactDetail, PostLink, Membership,    # noqa
                                  MembershipContactDetail, MembershipLink,          # noqa
                                  Event, EventLocation, VoteEvent)                  # noqa
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
    Division.objects.create('ocd-division/country:us', name='US')
    ak = Division.objects.create('ocd-division/country:us/state:ak', name='Alaska')
    Division.objects.create('ocd-division/country:us/state:ak/county:wild', name='Wild')
    Division.objects.create('ocd-division/country:us/state:ak/county:mild', name='Mild')
    Division.objects.create('ocd-division/country:us/state:ak/county:wild/place:a', name='A')
    Division.objects.create('ocd-division/country:us/state:ak/county:wild/place:b', name='B')
    Division.objects.create('ocd-division/country:us/state:ak/county:wild/school:a', name='A')
    Division.objects.create('ocd-division/country:us/state:ak/county:mild/place:a', name='A')
    Division.objects.create('ocd-division/country:us/state:ak/county:mild/place:a/x:y', name='A')

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
    str(o)
    assert o.id.startswith('ocd-organization/')
    assert o.pk == o.id
    p = Person.objects.create(name='test person')
    str(p)
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

    str(j)


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


@pytest.mark.django_db
def test_organization_get_parents():
    o1 = Organization.objects.create(name='National Organization on Bread-and-Cheese Products')
    o2 = Organization.objects.create(name='Committee on Pizza', parent=o1)
    o3 = Organization.objects.create(name='Subcommittee on Sicilian Pizza', parent=o2)

    assert list(o3.get_parents()) == [o2, o1]



@pytest.mark.django_db
def test_event_instance():
    div = Division.objects.create(
        id='ocd-division/country:us/state:mo',
        name='Missouri'
    )

    juris = Jurisdiction.objects.create(
        id="ocd-division/country:us/state:mo",
        name="Missouri State Senate",
        url="http://www.senate.mo.gov",
        division=div,
    )

    loc = EventLocation.objects.create(
        name="State Legislative Building",
        coordinates=Point(33.448040, -112.097379),
        jurisdiction=juris,
    )

    e = Event.objects.create(
        name="Meeting of the Committee on Energy",
        jurisdiction=juris,
        description="To discuss the pros/cons of wind farming.",
        classification='committee-meeting',
        start_time="2014-8-24 21:13:25",
        timezone='US/Central',
        status="passed",
        location=loc,
    )

    str(e)
    str(e.location)

    e.media.create(
        note="Recording of the meeting",
        date="2014-04-12",
        offset="19",
    )
    str(e.media.all()[0])

    e.links.create(
        note="EPA Website",
        url="http://www.epa.gov/",
    )
    str(e.links.all()[0])

    e.sources.create(
        note="scraped source",
        url="http://example.com/events",
    )
    str(e.sources.all()[0])
    
    ent1 = Organization.objects.create(name="Committee on Energy")
    ent2 = Person.objects.create(name="Andrew Tobin")
    e.participants.create(
        organization=ent1,
        note="Host Committee",
    )
    e.participants.create(
        person=ent2,
        note="Speaker",
    )
    for p in e.participants.all():
        str(p)
        p.entity_name
        p.entity_id

    e_a = e.agenda.create(
        description="Presentation by Director Henry Darwin, Arizona Department "
                    "of Environmental Quality, regarding the Environmental "
                    "Protection Agency (EPA) Clean Power Plan proposed rule",
        order=2,
        subjects=["epa", "green energy", "environmental issues"],
    )
    str(e_a)
    
    ent1 = Person.objects.create(name="Henry Darwin")
    ent2 = Organization.objects.create(name="Environmental Protection Agency (EPA)")
    e_a.related_entities.create(
        person=ent1,
    )
    e_a.related_entities.create(
        organization=ent2,
    )
    for r_e in e_a.related_entities.all():
        str(r_e)
        r_e.entity_name
        r_e.entity_id 

    e_a_med = e_a.media.create(
        note="Recording Darwin presentation",
        date="2014-04-12",
    )
    str(e_a_med)
    
    e_a_med.links.create(
        media_type="video/mp4",
        url="http://example.com/video.mp4",
    )
    str(e_a_med.links.all()[0])


@pytest.mark.django_db
def test_vote_event_instance():
    div = Division.objects.create(
        id='ocd-division/country:us/state:mo',
        name='Missouri'
    )
    juris = Jurisdiction.objects.create(
        id="ocd-division/country:us/state:mo",
        name="Missouri State Senate",
        url="http://www.senate.mo.gov",
        division=div,
    )
    l_s = LegislativeSession.objects.create(
        jurisdiction=juris,
        identifier=2017,
        name="2017 Session",
        start_date="2017-01-04",
        end_date="2017-05-25",
    )
    str(l_s)

    o = Organization.objects.create(name="Missouri State Senate")

    v_e = VoteEvent.objects.create(
        identifier="Roll Call #2372",
        motion_text="That the House do now proceed to the Orders of the Day.",
        start_date="2017-02-16",
        result="pass",
        organization=o,
        legislative_session=l_s,
    )
    str(v_e)

    v_e.counts.create(
        option="yes",
        value=36,
    )
    str(v_e.counts.all()[0])

    p = Person.objects.create(name="Maria Chappelle-Nadal")
    v_e.votes.create(
        option="yes",
        voter_name="Maria Chappelle-Nadal",
        voter=p,
    )
    str(v_e.votes.all()[0])