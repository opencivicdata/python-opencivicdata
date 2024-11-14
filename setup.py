#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = ["Django>=4.2", "psycopg2-binary"]

extras_require = {
    "dev": ["pytest>=3.6", "pytest-cov", "pytest-django", "coveralls==3.2.0", "flake8"]
}

setup(
    name="opencivicdata",
    version="3.4.0",
    author="James Turk",
    author_email="james@openstates.org",
    license="BSD",
    description="python opencivicdata library",
    long_description="",
    url="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
