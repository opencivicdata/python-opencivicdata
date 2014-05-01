from __future__ import print_function
import os
import csv
from subprocess import check_call
from optparse import make_option

from django.db import transaction, connection
from django.core.management.base import BaseCommand, CommandError

from ...models import Division


def _ocd_id_to_args(ocd_id):
    pieces = ocd_id.split('/')
    if pieces.pop(0) != 'ocd-division':
        raise Exception('ID must start with ocd-division/')
    country = pieces.pop(0)
    if not country.startswith('country:'):
        raise Exception('Second part of ID must be country:')
    else:
        country = country.replace('country:', "")
    n = 1
    args = {'country': country}
    for piece in pieces:
        type_, id_ = piece.split(':')
        args['subtype%s' % n] = type_
        args['subid%s' % n] = id_
        n += 1
    return args


def load_divisions(country):
    count = 0
    filename = os.path.join(os.path.dirname(__file__), '..', '..', 'division-ids', 'identifiers',
                            'country-{}.csv'.format(country))
    print('loading ' + filename)

    objects = []
    # country csv
    for row in csv.DictReader(open(filename, encoding='utf8')):
        args = _ocd_id_to_args(row['id'])
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
