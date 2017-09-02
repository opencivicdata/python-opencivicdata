#!/bin/sh
set -e
export PYTHONPATH=.; py.test --cov opencivicdata --ds=opencivicdata.tests.test_settings --cov-report html --cov-config=.coveragerc
coverage report -m
