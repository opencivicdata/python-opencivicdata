import pytest


@pytest.mark.django_db
def test_election_str(election):
    assert election.name in str(election)


@pytest.mark.django_db
def test_election_identifier_str(election_identifier):
    assert election_identifier.identifier in str(election_identifier)


@pytest.mark.django_db
def test_candidate_contest_str(candidate_contest):
    assert candidate_contest.name in str(candidate_contest)


@pytest.mark.django_db
def test_candidate_contest_post_str(candidate_contest_post):
    assert candidate_contest_post.post.label in str(candidate_contest_post)


@pytest.mark.django_db
def test_candidacy_str(candidacy):
    assert candidacy.candidate_name in str(candidacy)


@pytest.mark.django_db
def test_candidacy_election(candidacy, election):
    assert candidacy.election == election


@pytest.mark.django_db
def test_candidate_contest_post_candidacies(candidate_contest_post, person):
    assert candidate_contest_post.candidacies.count() == 0


@pytest.mark.django_db
def test_candidate_contest_identifier_str(candidate_contest_identifier):
    assert candidate_contest_identifier.identifier in str(candidate_contest_identifier)


@pytest.mark.django_db
def test_ballot_measure_contest_str(ballot_measure_contest):
    assert ballot_measure_contest.name in str(ballot_measure_contest)


@pytest.mark.django_db
def test_ballot_measure_contest_identifier_str(ballot_measure_contest_identifier):
    assert ballot_measure_contest_identifier.identifier in str(
        ballot_measure_contest_identifier
    )


@pytest.mark.django_db
def test_ballot_measure_contest_option_str(ballot_measure_contest_option):
    assert ballot_measure_contest_option.text in str(ballot_measure_contest_option)


@pytest.mark.django_db
def test_retention_contest_str(retention_contest):
    assert retention_contest.name in str(retention_contest)


@pytest.mark.django_db
def test_retention_contest_identifier_str(retention_contest_identifier):
    assert retention_contest_identifier.identifier in str(retention_contest_identifier)


@pytest.mark.django_db
def test_retention_contest_option_str(retention_contest_option):
    assert retention_contest_option.text in str(retention_contest_option)


@pytest.mark.django_db
def test_party_contest_str(party_contest):
    assert party_contest.name in str(party_contest)


@pytest.mark.django_db
def test_party_contest_identifier_str(party_contest_identifier):
    assert party_contest_identifier.identifier in str(party_contest_identifier)


@pytest.mark.django_db
def test_party_contest_option_str(party_contest_option):
    assert party_contest_option.party.name in str(party_contest_option)
