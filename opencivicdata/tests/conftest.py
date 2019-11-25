import pytest
from datetime import date, datetime
from django.contrib.gis.geos import Point
from opencivicdata.core.models import (
    Jurisdiction,
    Division,
    Membership,
    Organization,
    Person,
    Post,
)
from opencivicdata.legislative.models import (
    LegislativeSession,
    Event,
    EventLocation,
    VoteEvent,
    Bill,
)
from opencivicdata.elections.models import (
    Election,
    ElectionIdentifier,
    Candidacy,
    CandidateContest,
    CandidateContestPost,
    CandidateContestIdentifier,
    BallotMeasureContest,
    BallotMeasureContestOption,
    BallotMeasureContestIdentifier,
    RetentionContest,
    RetentionContestOption,
    RetentionContestIdentifier,
    PartyContest,
    PartyContestOption,
    PartyContestIdentifier,
)


@pytest.fixture
def division():
    div = Division.objects.create(
        id="ocd-division/country:us/state:mo", name="Missouri"
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
def organization():
    org = Organization.objects.create(name="Missouri State Senate")
    return org


@pytest.fixture
def bill(legislative_session):
    b = Bill.objects.create(
        legislative_session=legislative_session,
        identifier="HR 3590",
        title="The Patient Protection and Affordable Care Act",
    )
    return b


@pytest.fixture
def vote_event(legislative_session, organization):
    v_e = VoteEvent.objects.create(
        motion_text="That the House do now proceed to the Orders of the Day.",
        start_date="2017-02-16",
        result="pass",
        organization=organization,
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
        classification="committee-meeting",
        start_date=datetime.utcnow().isoformat().split(".")[0],
        status="passed",
        location=event_location,
    )
    return e


@pytest.fixture
def party():
    p = Organization.objects.create(name="Republican", classification="party")
    return p


@pytest.fixture
def person():
    p = Person.objects.create(
        name="Arnold Schwarzenegger", sort_name="Schwarzenegger, Arnold"
    )
    return p


@pytest.fixture
def post(organization):
    p = Post.objects.create(organization=organization, label="Governor")
    return p


@pytest.fixture
def membership(organization, post, person):
    m = Membership.objects.create(organization=organization, post=post, person=person)
    return m


@pytest.fixture
def election(division):
    elec = Election.objects.create(
        name="2016 General", date=date(2016, 11, 8), division=division
    )
    return elec


@pytest.fixture
def election_identifier(election):
    elec_id = ElectionIdentifier.objects.create(
        election=election, scheme="calaccess_election_id", identifier="65"
    )
    return elec_id


@pytest.fixture
def candidate_contest(election, division):
    cc = CandidateContest.objects.create(
        name="Governor", division=division, election=election, number_elected=1
    )
    return cc


@pytest.fixture
def candidate_contest_post(candidate_contest, post):
    ccp = CandidateContestPost.objects.create(contest=candidate_contest, post=post)
    return ccp


@pytest.fixture
def candidacy(candidate_contest, post, person, party):
    cand = Candidacy.objects.create(
        person=person,
        contest=candidate_contest,
        post=post,
        candidate_name=person.name,
        party=party,
    )
    return cand


@pytest.fixture
def candidate_contest_identifier(candidate_contest):
    cc_id = CandidateContestIdentifier.objects.create(
        contest=candidate_contest, scheme="calaccess_contest_id", identifier="GOV"
    )
    return cc_id


@pytest.fixture
def ballot_measure_contest(election, division):
    bmc = BallotMeasureContest.objects.create(
        name="Proposition 060- Adult Films. Condoms. Health Requirements. Initiative Statute.",
        division=division,
        election=election,
    )
    return bmc


@pytest.fixture
def ballot_measure_contest_identifier(ballot_measure_contest):
    bmc_id = BallotMeasureContestIdentifier.objects.create(
        contest=ballot_measure_contest,
        scheme="calaccess_measure_id",
        identifier="1376195",
    )
    return bmc_id


@pytest.fixture
def ballot_measure_contest_option(ballot_measure_contest):
    opt = BallotMeasureContestOption.objects.create(
        contest=ballot_measure_contest, text="yes"
    )
    return opt


@pytest.fixture
def retention_contest(election, division, membership):
    rc = RetentionContest.objects.create(
        name="2003 Recall Question",
        division=division,
        election=election,
        membership=membership,
    )
    return rc


@pytest.fixture
def retention_contest_identifier(retention_contest):
    rc_id = RetentionContestIdentifier.objects.create(
        contest=retention_contest, scheme="calaccess_measure_id", identifier="1256382"
    )
    return rc_id


@pytest.fixture
def retention_contest_option(retention_contest):
    opt = RetentionContestOption.objects.create(contest=retention_contest, text="yes")
    return opt


@pytest.fixture
def party_contest(election, division):
    pc = PartyContest.objects.create(
        name="Elections for the 20th Knesset", division=division, election=election
    )
    return pc


@pytest.fixture
def party_contest_identifier(party_contest):
    pc_id = PartyContestIdentifier.objects.create(
        contest=party_contest, scheme="party_contest_id", identifier="pc09"
    )
    return pc_id


@pytest.fixture
def party_contest_option(party_contest, party):
    opt = PartyContestOption.objects.create(contest=party_contest, party=party)
    return opt
