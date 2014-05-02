import pytest
from ..models import (Jurisdiction, JurisdictionSession, Division,
                      Organization, OrganizationIdentifier, OrganizationName,
                      OrganizationContactDetail, OrganizationSource,
                      Person, PersonIdentifier, PersonName, PersonContactDetail, PersonLink,
                      PersonSource,
                      Post, PostContactDetail, PostLinks,
                      Membership, MembershipContactDetail, MembershipLink)


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
def test_simple_division():
    division_id = 'ocd-division/country:us/state:ak/county:wild'
    d = Division.objects.create(id=division_id, display_name='Wild County',
                                **Division.subtypes_from_id(division_id)[0])
    assert division_id in str(d)
