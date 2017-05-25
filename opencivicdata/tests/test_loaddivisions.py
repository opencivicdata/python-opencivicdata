import pytest
from django.core.management import call_command
from opencivicdata.core.models import Division


@pytest.mark.django_db
def test_loaddivisions():
    assert Division.objects.count() == 0
    call_command('loaddivisions', 'in')
    assert Division.objects.count() > 0
    assert Division.objects.count() == Division.objects.filter(country='in').count()
    assert Division.objects.filter(country='in', subtype1='state', subtype2='').count() == 28

    # Include a (very weak) check for idempotency
    call_command('loaddivisions', 'in')
    assert Division.objects.filter(country='in', subtype1='state', subtype2='').count() == 28
