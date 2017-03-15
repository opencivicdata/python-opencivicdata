import pytest
from datetime import datetime
from django.contrib.gis.geos import Point
from opencivicdata.models import (
    Jurisdiction,
    LegislativeSession,
    Division,
    Organization,
    Event,
    EventLocation,
    VoteEvent,
    Bill,
)


@pytest.fixture
def division():
    div = Division.objects.create(
        id='ocd-division/country:us/state:mo',
        name='Missouri'
    )
    return div


@pytest.fixture
def jurisdiction(division):
    juris = Jurisdiction.objects.create(
        id="ocd-division/country:us/state:mo",
        name="Missouri State Senate",
        url="http://www.senate.mo.gov",
        division=division,
    )
    return juris


@pytest.fixture
def legislative_session(jurisdiction):
    l_s = LegislativeSession.objects.create(
        jurisdiction=jurisdiction,
        identifier=2017,
        name="2017 Session",
        start_date="2017-01-04",
        end_date="2017-05-25",
    )
    return l_s


@pytest.fixture
def bill(legislative_session):
    b = Bill.objects.create(
        legislative_session=legislative_session,
        identifier="HR 3590",
        title="The Patient Protection and Affordable Care Act",
    )
    return b


@pytest.fixture
def vote_event(legislative_session):
    o = Organization.objects.create(name="Missouri State Senate")
    v_e = VoteEvent.objects.create(
        motion_text="That the House do now proceed to the Orders of the Day.",
        start_date="2017-02-16",
        result="pass",
        organization=o,
        legislative_session=legislative_session,
    )
    return v_e


@pytest.fixture
def event_location(jurisdiction):
    loc = EventLocation.objects.create(
        name="State Legislative Building",
        coordinates=Point(33.448040, -112.097379),
        jurisdiction=jurisdiction,
    )
    return loc


@pytest.fixture
def event(jurisdiction, event_location):
    e = Event.objects.create(
        name="Meeting of the Committee on Energy",
        jurisdiction=jurisdiction,
        description="To discuss the pros/cons of wind farming.",
        classification='committee-meeting',
        start_time=datetime.now(),
        timezone='US/Central',
        status="passed",
        location=event_location,
    )
    return e