import os

import pytest
from django.core.management import call_command

from opencivicdata.divisions import Division as FileDivision
from opencivicdata.core.models import Division


@pytest.mark.django_db
def test_loaddivisions(capsys):
    assert Division.objects.count() == 0

    call_command("loaddivisions", "in")

    assert Division.objects.count() > 0
    assert Division.objects.count() == Division.objects.filter(country="in").count()
    assert (
        Division.objects.filter(country="in", subtype1="state", subtype2="").count()
        == 29
    )

    # Include a (very weak) check for idempotency
    call_command("loaddivisions", "in")

    assert (
        Division.objects.filter(country="in", subtype1="state", subtype2="").count()
        == 29
    )

    # The FileDivision's cache is a mutable class attribute, which is shared
    # between instances. Reset it, so calling the command with a CSV specified
    # does not use divisions cached from previous runs.
    FileDivision._cache = {}

    test_dir = os.path.abspath(os.path.dirname(__file__))
    os.environ["OCD_DIVISION_CSV"] = os.path.join(
        test_dir, "fixtures", "country-in-subset.csv"
    )

    call_command("loaddivisions", "in")

    out, _ = capsys.readouterr()
    last_message = out.splitlines()[-1]

    assert last_message == "The DB contains all CSV contents; no work to be done!"

    # Unset the CSV environment variable so subsequent division tests reload
    # divisions from source instead of breaking.
    os.environ.pop("OCD_DIVISION_CSV")
