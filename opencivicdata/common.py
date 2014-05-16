"""
Module for declaration of common constants available throughout Open Civic Data code.
"""

import re

DIVISION_ID_REGEX = re.compile(r'^ocd-division/country:[a-z]{2}(/[^\W\d]+:[\w.~-]+)*$', re.U)
JURISDICTION_ID_REGEX = re.compile(r'^ocd-jurisdiction/country:[a-z]{2}(/[^\W\d]+:[\w.~-]+)*/\w+$',
                                   re.U)

# helper for making options-only lists
_keys = lambda allopts: [opt[0] for opt in allopts]

"""
Policy on addition of new types:

Because these lists are strictly enforced in lots of code for the purposes of data quality
we have a fairly liberal policy on amendment.

If a type is needed and is not duplicative of another type, it will be accepted.

At the moment, because of this policy, no method exists to extend these lists, instead we will
strive for them to be comprehensive.

The only exception to this would be translations, which should simply exist as translations of
the display name (2nd attribute).
"""

CONTACT_TYPE_CHOICES = (
    ('address', 'Postal Address'),
    ('email', 'Email'),
    ('url', 'URL'),
    ('text', 'Text Phone'),
    ('voice', 'Voice Phone'),
    ('video', 'Video Phone'),
    ('pager', 'Pager'),
    ('textphone', 'Device for people with hearing impairment'),
# NOTE: this list explicitly does not include RFC 6350s 'cell' as that is redundant with
# voice and the distinction will only lead to confusion.  contact_detail.note can be
# used to indicate if something is a home, work, cell, etc.
)
CONTACT_TYPES = _keys(CONTACT_TYPE_CHOICES)

ORGANIZATION_CLASSIFICATION_CHOICES = (
    ('legislature', 'Legislature'),
    ('party', 'Party'),
    ('committee', 'Committee'),
    ('commission', 'Commission'),
)
ORGANIZATION_CLASSIFICATIONS = _keys(ORGANIZATION_CLASSIFICATION_CHOICES)

BILL_CLASSIFICATION_CHOICES = (
    ('bill', 'Bill'),
    ('resolution', 'Resolution'),
    ('concurrent resolution', 'Concurrent Resolution'),
    ('joint resolution', 'Joint Resolution'),
    ('memorial', 'Memorial'),
)
BILL_CLASSIFICATIONS = _keys(BILL_CLASSIFICATION_CHOICES)

BILL_RELATION_TYPE_CHOICES = (
    ('companion', 'Companion'),             # a companion in another chamber
    ('prior-session', 'Prior Session'),     # an introduction from a prior session
    ('replaced-by', 'Replaced By'),         # a bill has been replaced by another
    ('replaces', 'Replaces'),               # a bill that replaces another
)
BILL_RELATION_TYPES = _keys(BILL_RELATION_TYPE_CHOICES)

BILL_ACTION_TYPE_CHOICES = (
    ('introduction', 'Introduced'),
    ('reading:1', 'First Reading'),
    ('reading:2', 'Second Reading'),
    ('reading:3', 'Third Reading'),
    # this list is notably incomplete!
)
BILL_ACTION_TYPES = _keys(BILL_ACTION_TYPE_CHOICES)

VOTE_CLASSIFICATION_CHOICES = (
    ('passage:bill', 'Bill Passage'),
    ('passage:amendment', 'Amendment Passage'),
    ('passage:veto-override', 'Veto Override'),
)
VOTE_CLASSIFICATIONS = _keys(VOTE_CLASSIFICATION_CHOICES)

VOTE_OPTION_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('abstain', 'Abstain'),
    ('paired', 'Paired'),
)
VOTE_OPTIONS = _keys(VOTE_OPTION_CHOICES)

VOTE_OUTCOME_CHOICES = (
    ('pass', 'Pass'),
    ('fail', 'Fail'),
)
VOTE_OUTCOMES = _keys(VOTE_OUTCOME_CHOICES)

# Possible Candidates for future inclusion:
# bill_version_types
# bill_document_types
