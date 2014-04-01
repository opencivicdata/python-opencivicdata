#!/usr/bin/env python
import os
import csv

PWD = os.path.abspath(os.path.dirname(__file__))
OCD_DIVISION_CSV = os.path.join(PWD, 'division-ids/identifiers/country-{}.csv')


class Division(object):

    _cache = {}

    @classmethod
    def get(self, id):
        return self._cache[id]

    @classmethod
    def load(self, country):
        for row in csv.DictReader(open(OCD_DIVISION_CSV.format(country))):
            same_as = row.pop('sameAs', None)
            if same_as:
                #divisions[same_as].names.append(row['id'])
                continue
            #same_as_note = row.pop('sameAsNote', None)
            Division(**row)
        return Division.get('ocd-division/country:' + country)

    def __init__(self, id, name, **kwargs):
        self._cache[id] = self
        self.id = id
        self.name = name
        valid_through = kwargs.pop('validThrough', None)
        if valid_through:
            self.valid_through = valid_through

        # set parent and _type
        parent, own_id = id.rsplit('/', 1)
        if parent == 'ocd-division':
            self.parent = None
        else:
            self.parent = self._cache[parent]
            self.parent._children.append(self)

        self._type = own_id.split(':')[0]

        # other attrs
        self.attrs = kwargs
        self.names = []
        self._children = []

    def children(self, _type=None):
        for d in self._children:
            if not _type or d._type == _type:
                yield d

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
