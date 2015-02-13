#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="opencivicdata-divisions",
      version='2015.02.13',
      py_modules=['opencivicdata.divisions'],
      author="James Turk",
      author_email='jturk@sunlightfoundation.com',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      packages=['opencivicdata.divisions'],
      include_package_data=True,
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   ],
      )
