#!/usr/bin/env python
import sys
import setuptools
from setuptools import setup, find_packages

install_requires = [
    'six',
    'Django>=1.11',
    'psycopg2',
]

extras_require = {
    'dev': [
      'pytest>=2.9',
      'pytest-cov',
      'pytest-django',
      'coveralls',
      'flake8',
    ],
}

if int(setuptools.__version__.split(".", 1)[0]) < 18:
    assert "bdist_wheel" not in sys.argv, "setuptools 18 required for wheels."
    # For legacy setuptools + sdist.
    if sys.version_info[0:2] <= (2, 7):
        install_requires.append("backports.csv")
else:
    extras_require[":python_version<='2.7'"] = ["backports.csv"]

setup(name="opencivicdata",
      version='2.1.2',
      author="James Turk",
      author_email='james@openstates.org',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      extras_require=extras_require,
      platforms=["any"],
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   ],
      )
