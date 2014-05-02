from __future__ import print_function
import io
import os
import csv
from subprocess import check_call
from optparse import make_option

from django.db import transaction, connection
from django.core.management.base import BaseCommand, CommandError

from ...models import Division


def load_divisions(country):
    count = 0
    filename = os.path.join(os.path.dirname(__file__), '..', '..', 'division-ids', 'identifiers',
                            'country-{}.csv'.format(country))
    print('loading ' + filename)

    objects = []
    # country csv
    for row in csv.DictReader(io.open(filename, encoding='utf8')):
        args, _ = Division.subtypes_from_id(row['id'])
        args['redirect_id'] = row.get('sameAs', None) or None
        objects.append(Division(id=row['id'], display_name=row['name'], **args))

    print(len(objects), 'divisions loaded from CSV')

    # delete old ids and add new ones all at once
    with transaction.atomic():
        Division.objects.filter(country=country).delete()
        Division.objects.bulk_create(objects, batch_size=10000)

    print(len(objects), 'divisions created')


class Command(BaseCommand):
    help = 'initialize a pupa database'

    def handle(self, *args, **options):
        for country in args:
            load_divisions(country)
