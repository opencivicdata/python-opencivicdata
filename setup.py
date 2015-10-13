#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="opencivicdata-django",
      version='0.7.1',
      author="James Turk",
      author_email='james.p.turk@gmail.com',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      packages=find_packages(),
      install_requires=[
          'Django>=1.9a1',
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
