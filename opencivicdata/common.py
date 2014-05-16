import re

DIVISION_ID_REGEX = re.compile(r'^ocd-division/country:[a-z]{2}(/[^\W\d]+:[\w.~-]+)*$', re.U)
JURISDICTION_ID_REGEX = re.compile(r'^ocd-jurisdiction/country:[a-z]{2}(/[^\W\d]+:[\w.~-]+)*/\w+$',
                                   re.U)
