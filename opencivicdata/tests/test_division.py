from .. import Division, us


def test_children():
    assert len(list(us.children('state'))) == 50


def test_get():
    wake = Division.get('ocd-division/country:us/state:nc/county:wake')
    assert wake.name == 'Wake County', wake.name
