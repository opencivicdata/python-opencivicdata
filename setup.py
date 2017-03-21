#!/usr/bin/env python
from setuptools import setup, __version__
import sys

# backports.csv required for Python 2.7
INSTALL_REQUIRES = []
EXTRAS_REQUIRE = {}

# conditionally pass install_requires arg if setuptools older than v18
if int(__version__.split(".", 1)[0]) < 18:
    if sys.version_info[0:2] == (2, 7):
        INSTALL_REQUIRES.append("backports.csv")
# otherwise pass extra_requires arg
else:
    EXTRAS_REQUIRE[":python_version=='2.7'"] = ["backports.csv"]

setup(name="opencivicdata-divisions",
      version='2017.3.22',
      py_modules=['opencivicdata.divisions'],
      author="James Turk",
      author_email='james@openstates.org',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      packages=['opencivicdata.divisions'],
      namespace_packages=['opencivicdata'],
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   ],
      )
