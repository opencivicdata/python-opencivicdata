import pytest
from opencivicdata.core.models import Jurisdiction, Division, Organization, Person
from django.core.exceptions import ValidationError


def test_division_subtypes_from_id():

    # simplest case
    assert Division.subtypes_from_id("ocd-division/country:us") == (
        {"country": "us"},
        1,
    )

    # ocd-divison part is optional
    assert Division.subtypes_from_id("country:us/state:ak/county:wild") == (
        {
            "country": "us",
            "subtype1": "state",
            "subid1": "ak",
            "subtype2": "county",
            "subid2": "wild",
        },
        3,
    )

    # country is not optional
    with pytest.raises(ValueError):
        Division.subtypes_from_id("state:nc/city:raleigh")


@pytest.mark.django_db
def test_division_create():
    division_id = "ocd-division/country:us/state:ak/county:wild"
    d = Division.objects.create(id=division_id, name="Wild County")
    assert d.country == "us"
    assert d.subtype1 == "state"
    assert d.subid1 == "ak"
    assert d.subtype2 == "county"
    assert d.subid2 == "wild"
    assert division_id in str(d)


@pytest.mark.django_db
def test_division_children_of():
    Division.objects.create("ocd-division/country:us", name="US")
    ak = Division.objects.create("ocd-division/country:us/state:ak", name="Alaska")
    Division.objects.create("ocd-division/country:us/state:ak/county:wild", name="Wild")
    Division.objects.create("ocd-division/country:us/state:ak/county:mild", name="Mild")
    Division.objects.create(
        "ocd-division/country:us/state:ak/county:wild/place:a", name="A"
    )
    Division.objects.create(
        "ocd-division/country:us/state:ak/county:wild/place:b", name="B"
    )
    Division.objects.create(
        "ocd-division/country:us/state:ak/county:wild/school:a", name="A"
    )
    Division.objects.create(
        "ocd-division/country:us/state:ak/county:mild/place:a", name="A"
    )
    Division.objects.create(
        "ocd-division/country:us/state:ak/county:mild/place:a/x:y", name="A"
    )

    # simplest ==
    assert Division.objects.children_of("ocd-division/country:us")[0].id == ak.id

    # 3 divisions within wild county
    assert (
        Division.objects.children_of(
            "ocd-division/country:us/state:ak/county:wild"
        ).count()
        == 3
    )

    # only one school in wild county
    assert (
        Division.objects.children_of(
            "ocd-division/country:us/state:ak/county:wild", subtype="school"
        ).count()
        == 1
    )

    # 6 divisions beneath alaska up to 2 levels
    assert (
        Division.objects.children_of(
            "ocd-division/country:us/state:ak", depth=2
        ).count()
        == 6
    )

    # 7 divisions beneath alaska up to 3 levels
    assert (
        Division.objects.children_of(
            "ocd-division/country:us/state:ak", depth=3
        ).count()
        == 7
    )


@pytest.mark.django_db
def test_ocdid_default():
    o = Organization.objects.create(name="test org")
    assert o.id.startswith("ocd-organization/")
    assert o.pk == o.id
    p = Person.objects.create(name="test person")
    assert p.id.startswith("ocd-person/")


@pytest.mark.django_db
def test_ocdid_default_nondup():
    """ ensure that defaults actually vary """
    p1 = Person(name="test person 1")
    p2 = Person(name="test person 2")
    assert p1.id != p2.id


@pytest.mark.django_db
def test_ocdid_validation_jurisdiction():
    # this fails
    with pytest.raises(ValidationError):
        j = Jurisdiction(
            name="test juris",
            id="ocd-division/country:us/test:something/else",
            url="http://example.com",
        )
        j.full_clean(exclude=["division"])

    # this succeeds
    j = Jurisdiction(
        name="test juris",
        id="ocd-jurisdiction/country:us/test:something/else",
        url="http://example.com",
    )
    j.full_clean(exclude=["division"])

    assert str(j) == j.name


@pytest.mark.django_db
def test_ocdid_validation_other():
    # this test should handle everything that isn't a jurisdiction

    # this succeeds
    o = Organization(name="test org")
    o.full_clean(exclude=["parent", "jurisdiction"])

    # this raises
    with pytest.raises(ValidationError):
        o = Organization(name="this is a test", id="ocd-organization/3")
        o.full_clean(exclude=["parent", "jurisdiction"])


@pytest.mark.django_db
def test_organization_get_parents():
    o1 = Organization.objects.create(
        name="National Organization on Bread-and-Cheese Products"
    )
    o2 = Organization.objects.create(name="Committee on Pizza", parent=o1)
    o3 = Organization.objects.create(name="Subcommittee on Sicilian Pizza", parent=o2)

    assert list(o3.get_parents()) == [o2, o1]


@pytest.mark.django_db
def test_organization_str():
    o = Organization.objects.create(name="test org")
    assert "test org" in str(o)


@pytest.mark.django_db
def test_organization_contact_details():
    o = Organization.objects.create(name="test org")
    o.contact_details.create(type="email", value="info@test.org")

    assert "Email" in str(o.contact_details.all()[0])
    assert "info@test.org" in str(o.contact_details.all()[0])


@pytest.mark.django_db
def test_organization_other_name():
    o = Organization.objects.create(name="test org")
    o.other_names.create(name="tester org")

    assert "tester org" in str(o.other_names.all()[0])


@pytest.mark.django_db
def test_organization_identifier():
    o = Organization.objects.create(name="test org")
    o.identifiers.create(identifier="US0123456789", scheme="ISIN")

    assert "US0123456789" in str(o.identifiers.all()[0])
    assert "test org" in str(o.identifiers.all()[0])


@pytest.mark.django_db
def test_organization_post():
    o = Organization.objects.create(name="test org")
    o.posts.create(label="CEO")

    assert "CEO" in str(o.posts.all()[0])
    assert "test org" in str(o.posts.all()[0])


@pytest.mark.django_db
def test_organization_membership():
    o = Organization.objects.create(name="test org")
    p = Person.objects.create(name="test person")

    o.memberships.create(person=p, role="CEO")

    assert "CEO" in str(o.memberships.all()[0])
    assert "test person" in str(o.memberships.all()[0])
    assert "test org" in str(o.memberships.all()[0])
    assert len(o.get_current_members()) == 1
    assert len(Person.objects.member_of("test org")) == 1
    assert len(Person.objects.member_of(o.id)) == 1


@pytest.mark.django_db
def test_person_str(person):
    assert person.name in str(person)


@pytest.mark.django_db
def test_legislative_session_str(legislative_session):
    assert legislative_session.name in str(legislative_session)


@pytest.mark.django_db
def test_vote_event_str(vote_event):
    assert vote_event.motion_text in str(vote_event)
    # test adding identifier and alternate string repr
    vote_event.identifier = "Roll Call #2372"
    vote_event.save()
    assert "Roll Call #2372" in str(vote_event)


@pytest.mark.django_db
def test_vote_event_count(vote_event):
    vote_event.counts.create(option="yes", value=36)
    assert "yes" in str(vote_event.counts.all()[0])


@pytest.mark.django_db
def test_vote_event_vote(vote_event):
    p = Person.objects.create(name="Maria Chappelle-Nadal")
    vote_event.votes.create(option="yes", voter_name="Maria Chappelle-Nadal", voter=p)
    assert "Maria Chappelle-Nadal" in str(vote_event.votes.all()[0])


@pytest.mark.django_db
def test_bill_str(bill):
    assert bill.identifier in str(bill)


@pytest.mark.django_db
def test_bill_abstract(bill):
    bill.abstracts.create(
        abstract="This is the Senate's health care bill. The bill started off "
        "with text regarding an unrelated matter but the Senate is "
        "co-opted this bill as a vehicle for passage of their reform and "
        "changed the text in whole to the health care bill. They do this "
        "because the Constitution requires all revenue bills to start in "
        "the House, and their health reform plan involves revenue. So "
        "they have chosen to work off of a bill that started in the "
        "House, even if that bill is unrelated.",
        note="Library of Congress Summary",
    )
    assert bill.identifier in str(bill.abstracts.all()[0])


@pytest.mark.django_db
def test_bill_title(bill):
    o_t = bill.other_titles.create(title="Affordable Care Act")
    assert o_t.title in str(o_t)
    assert bill.identifier in str(o_t)


@pytest.mark.django_db
def test_bill_sponsorship(bill):
    spon = bill.sponsorships.create(classification="sponsor", name="Nancy Pelosi")
    assert spon.name in str(spon)
    assert bill.identifier in str(spon)


@pytest.mark.django_db
def test_bill_identifier(bill):
    bill.other_identifiers.create(identifier="1001", scheme="senate_clerk_id")
    assert "1001" in str(bill.other_identifiers.all()[0])


@pytest.mark.django_db
def test_related_bill(bill):
    r_b = bill.related_bills.create(
        legislative_session=bill.legislative_session,
        identifier="SB 22",
        relation_type="companion",
    )
    assert r_b.relation_type in str(r_b)
    assert bill.identifier in str(r_b)


@pytest.mark.django_db
def test_bill_action(bill):
    o = Organization.objects.create(name="Missouri State Senate")
    a = bill.actions.create(
        organization=o,
        description="Third Reading and Final Passage",
        date="2016-02-16",
        order=1,
    )
    assert a.date in str(a)
    assert bill.identifier in str(a)

    # test adding related entity to bill action
    p = Person.objects.create(name="Maria Chappelle-Nadal")
    a.related_entities.create(person=p, name=p.name, entity_type="person")
    assert p.name in str(a.related_entities.all()[0])


@pytest.mark.django_db
def test_bill_version_with_links(bill):
    v = bill.versions.create(note="Engrossed", date="2017-03-15")
    assert v.date in str(v)
    assert bill.identifier in str(v)

    # test adding link bill version
    v.links.create(
        url="http://committee.example.com/billversion1.pdf",
        media_type="application/pdf",
    )
    assert "http://committee.example.com/billversion1.pdf" in str(v.links.all()[0])
    assert bill.identifier in str(v.links.all()[0])


@pytest.mark.django_db
def test_bill_document_with_links(bill):
    doc = bill.documents.create(note="Fiscal Note", date="2017-03-01")
    assert bill.identifier in str(doc)

    # test adding link bill version
    doc.links.create(
        url="http://committee.example.com/bill_document.pdf",
        media_type="application/pdf",
    )
    assert "http://committee.example.com/bill_document.pdf" in str(doc.links.all()[0])
    assert bill.identifier in str(doc.links.all()[0])


@pytest.mark.django_db
def test_event_str(event):
    assert event.name in str(event)
    assert event.start_date in str(event)


@pytest.mark.django_db
def test_event_location_str(event_location):
    assert event_location.name in str(event_location)


@pytest.mark.django_db
def test_event_participant_person(event):
    p = Person.objects.create(name="Andrew Tobin")
    e_p = event.participants.create(
        name=p.name, person=p, entity_type="person", note="Speaker"
    )
    assert e_p.name in str(e_p)
    assert e_p.name in e_p.entity_name
    assert e_p.entity_id
    # remove entity_type value and re-try
    e_p.entity_type = ""
    assert e_p.name in e_p.entity_name
    assert e_p.entity_id is None


@pytest.mark.django_db
def test_event_participant_organization(event):
    o = Organization.objects.create(name="Committee on Energy")
    e_p = event.participants.create(
        name=o.name, organization=o, entity_type="organization", note="Host Committee"
    )
    assert e_p.name in str(e_p)
    assert e_p.name in e_p.entity_name
    assert e_p.entity_id
    # remove entity_type value and re-try
    e_p.entity_type = ""
    assert e_p.name in e_p.entity_name
    assert e_p.entity_id is None


@pytest.mark.django_db
def test_event_link(event):
    event.links.create(note="EPA Website", url="http://www.epa.gov/")
    assert "http://www.epa.gov/" in str(event.links.all()[0])


@pytest.mark.django_db
def test_event_media_w_links(event):
    # test adding media to event
    e_m = event.media.create(
        note="Recording of the meeting", date="2014-04-12", offset="19"
    )
    assert "Recording of the meeting" in str(e_m)

    # test adding link event media
    e_m.links.create(media_type="video/webm", url="http://example.com/video.webm")
    assert "http://example.com/video.webm" in str(e_m.links.all()[0])


@pytest.mark.django_db
def test_event_document_w_links(event):
    # test adding document to event
    e_d = event.documents.create(date="2014-04-12", note="Agenda")
    assert "Agenda" in str(e_d)
    assert event.name in str(e_d)

    # test adding link to event document
    e_d.links.create(
        url="http://committee.example.com/agenda.pdf", media_type="application/pdf"
    )
    assert "http://committee.example.com/agenda.pdf" in str(e_d.links.all()[0])
    assert e_d.note in str(e_d.links.all()[0])


@pytest.mark.django_db
def test_event_agenda(event, vote_event, bill):
    # test adding agenda item to event
    e_a = event.agenda.create(
        description="Presentation by Director Henry Darwin, Arizona Department "
        "of Environmental Quality, regarding the Environmental "
        "Protection Agency (EPA) Clean Power Plan proposed rule",
        order=2,
        subjects=["epa", "green energy", "environmental issues"],
    )
    assert event.name in str(e_a)

    # test adding media to event agenda item
    e_a_med = e_a.media.create(note="Recording Darwin presentation", date="2014-04-12")
    assert "Recording Darwin presentation" in str(e_a_med)

    # test adding link to event agenda item media
    e_a_med.links.create(media_type="video/mp4", url="http://example.com/video.mp4")
    assert "http://example.com/video.mp4" in str(e_a_med.links.all()[0])

    # test adding related entities to event agenda
    e_a.related_entities.create(bill=bill, entity_type="bill", name=bill.identifier)
    e_a.related_entities.create(
        vote_event=vote_event, entity_type="vote", name=vote_event.identifier
    )
    for r_e in e_a.related_entities.all():
        assert r_e.name in str(r_e)
        assert r_e.name in r_e.entity_name
        assert r_e.entity_id
        # remove entity_type value and re-try
        r_e.entity_type = ""
        assert r_e.name in r_e.entity_name
        assert r_e.entity_id is None
