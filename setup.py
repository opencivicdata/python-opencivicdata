#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="opencivicdata-django",
      version='0.8.1',
      author="James Turk",
      author_email='james.p.turk@gmail.com',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      py_modules=['opencivicdata.apps', 'opencivicdata.common'],
      packages=['opencivicdata.admin',
                'opencivicdata.management',
                'opencivicdata.management.commands',
                'opencivicdata.migrations',
                'opencivicdata.models',
                'opencivicdata.tests'],
      # ugly hack b/c this is a namespace package
      data_files=[('opencivicdata/templates/opencivicdata/admin/', [
          'opencivicdata/templates/opencivicdata/admin/merge.html',
          'opencivicdata/templates/opencivicdata/admin/unresolved.html',
          'opencivicdata/templates/opencivicdata/admin/unresolved-confirm.html',
      ])],
      install_requires=[
          'Django>=1.9rc2',
          'psycopg2',
          'opencivicdata-divisions',
      ],
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.4",
                   ],
      )
