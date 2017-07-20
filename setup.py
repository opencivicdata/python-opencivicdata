#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

install_requires = [
    'six',
    'Django>=1.9',
    'psycopg2',
]

if sys.version_info[0] == 2:
    install_requires.append('backports.csv')


setup(name="opencivicdata",
      version='2.0.0',
      author="James Turk",
      author_email='james@openstates.org',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      extras_require={
          'dev': [
            'pytest>=2.9',
            'pytest-cov',
            'pytest-django',
            'coveralls',
            'flake8',
          ],
      },
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   ],
      )
