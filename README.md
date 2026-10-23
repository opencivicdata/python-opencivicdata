python-opencivicdata
====================

[![Build Status](https://travis-ci.com/opencivicdata/python-opencivicdata.svg?branch=master)](https://travis-ci.com/opencivicdata/python-opencivicdata)
[![Coverage Status](https://coveralls.io/repos/opencivicdata/python-opencivicdata/badge.png?branch=master)](https://coveralls.io/r/opencivicdata/python-opencivicdata?branch=master)
[![PyPI](https://img.shields.io/pypi/v/opencivicdata.svg)](https://pypi.python.org/pypi/opencivicdata)

Python utilities (including Django models) for implementing the
Open Civic Data specification.

**Requires Django >= 4.2 and Python >= 3.10 (Django 6.0 requires Python >= 3.12), pin to <3.0 for older versions**

To use the models in your Django project, add `django.contrib.postgres` and the
apps you need to `INSTALLED_APPS` and use the PostGIS database backend:

```python
INSTALLED_APPS = [
    ...
    "django.contrib.postgres",
    "opencivicdata.core.apps.BaseConfig",
    "opencivicdata.legislative.apps.BaseConfig",
    "opencivicdata.elections.apps.BaseConfig",
]

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        ...
    }
}
```

The Organization, Person, Membership, Post, and VoteEvent models and related models are based on the [Popolo specification](http://popoloproject.com/).

To run tests on this project: ./run-tests.sh
