#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="opencivicdata",
      version='1.0.0',
      author="James Turk",
      author_email='james@openstates.org',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'Django>=1.9',
          'psycopg2',
      ],
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
