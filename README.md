python-opencivicdata
====================

[![Build Status](https://travis-ci.org/opencivicdata/python-opencivicdata.svg?branch=master)](https://travis-ci.org/opencivicdata/python-opencivicdata)
[![Coverage Status](https://coveralls.io/repos/opencivicdata/python-opencivicdata/badge.png?branch=master)](https://coveralls.io/r/opencivicdata/python-opencivicdata?branch=master)
[![PyPI](https://img.shields.io/pypi/v/opencivicdata.svg)](https://pypi.python.org/pypi/opencivicdata)

Python utilities (including Django models) for implementing the
Open Civic Data specification.

**Requires Django >=1.11 and Python 2.7 or >= 3.5**

**As of 2.3.0 we recommend Postgres >= 10, changes that break 9.x will no longer be fixed**

The Organization, Person, Membership, Post, and VoteEvent models and related models are based on the [Popolo specification](http://popoloproject.com/).

To run tests on this project: ./run-tests.sh
