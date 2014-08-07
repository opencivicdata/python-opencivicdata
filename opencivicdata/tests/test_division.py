import sys
import pytest
from ..divisions import Division


@pytest.mark.skipif(sys.version_info < (3,3), reason="requires python3.3")
def test_get():
    wake = Division.get('ocd-division/country:us/state:nc/county:wake')
    assert wake.name == 'Wake County'
    assert wake.name in str(wake)


@pytest.mark.skipif(sys.version_info < (3,3), reason="requires python3.3")
def test_children():
    us = Division.get('ocd-division/country:us')
    assert len(list(us.children('state', duplicates=False))) == 50
