from __future__ import print_function

from django.db import transaction
from django.core.management.base import BaseCommand

from opencivicdata.divisions import Division as FileDivision
from ...models import Division


def to_db(fd):
    """ convert a FileDivision to a Division """
    args, _ = Division.subtypes_from_id(fd.id)
    if fd.sameAs:
        args['redirect_id'] = fd.sameAs
    return Division(id=fd.id, name=fd.name, **args)


def load_divisions(country):
    existing_divisions = Division.objects.filter(country=country)

    country_division = FileDivision.get('ocd-division/country:{}'.format(country))
    objects = [to_db(country_division)]

    for child in country_division.children(levels=100):
        objects.append(to_db(child))

    print('{} divisions found in the CSV, and {} already in the DB'.
          format(len(objects), existing_divisions.count()))

    if set(objects) == set(existing_divisions):
        print('The CSV and the DB contents are exactly the same; no work to be done!')
    else:
        # delete old ids and add new ones all at once
        with transaction.atomic():
            Division.objects.filter(country=country).delete()
            Division.objects.bulk_create(objects, batch_size=10000)
        print('{} divisions created'.format(len(objects)))


class Command(BaseCommand):
    help = 'initialize a pupa database'

    def add_arguments(self, parser):
        parser.add_argument('countries', nargs='+', type=str)

    def handle(self, *args, **options):
        for country in options['countries']:
            load_divisions(country)
