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

    country = FileDivision.get('ocd-division/country:{}'.format(country))
    objects = [to_db(country)]

    for child in country.children(levels=100):
        objects.append(to_db(child))

    print('{} divisions found in the CSV, and {} already in the DB'.
          format(len(objects), existing_divisions.count()))

    if set(objects) == set(existing_divisions):
        print('The CSV and the DB contents are exactly the same; no work to be done!')
    else:
        # delete old ids and add new ones all at once
        with transaction.atomic():
            Division.objects.filter(country=country).delete()
            for object_ in objects:
                object_.save()
            # Division.objects.bulk_create(objects, batch_size=10000)
            # XXX: The above line (bulk_create) ends up causing pk consistency
            #      issues when doing an update, even though we did a delete
            #      and the PK is clear. The .save() on each shockingly
            #      works. I'm switching this until this is entirely
            #      understood.
        print('{} divisions created'.format(len(objects)))


class Command(BaseCommand):
    help = 'initialize a pupa database'

    def add_arguments(self, parser):
        parser.add_argument('countries', nargs='+', type=str)

    def handle(self, *args, **options):
        for country in options['countries']:
            load_divisions(country)
