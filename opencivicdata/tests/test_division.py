#!/u/bin/env python
# -*- coding: utf-8 -*-
from opencivicdata.divisions import Division


def test_get():
    div = Division.get('ocd-division/country:de/land:bw/wahlkreis:bad_kissingen')
    assert div.name == 'Bad Kissingen'
    assert div.name in str(div)


def test_children():
    us = Division.get('ocd-division/country:ua')
    assert len(list(us.children('region', duplicates=False))) == 25
