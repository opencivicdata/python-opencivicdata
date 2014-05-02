from django.db import models


class DivisionManager(models.Manager):

    def children_of(self, division_id, subtype=None, depth=1):
        query, n = Division.subtypes_from_id(division_id)

        # only get children
        if subtype:
            query['subtype{0}'.format(n)] = subtype
        else:
            query['subtype{0}__isnull'.format(n)] = False
        query['subid{0}__isnull'.format(n)] = False

        # allow for depth wildcards
        n += depth

        # ensure final field is null
        query['subtype{0}__isnull'.format(n)] = True
        query['subid{0}__isnull'.format(n)] = True

        return self.filter(**query)


class Division(models.Model):
    objects = DivisionManager()

    id = models.CharField(max_length=300, primary_key=True)
    display_name = models.CharField(max_length=300)
    redirect = models.ForeignKey('self', null=True)
    country = models.CharField(max_length=2)

    # up to 7 pieces of the id that are searchable
    subtype1 = models.CharField(max_length=50, blank=True)
    subid1 = models.CharField(max_length=100, blank=True)
    subtype2 = models.CharField(max_length=50, blank=True)
    subid2 = models.CharField(max_length=100,  blank=True)
    subtype3 = models.CharField(max_length=50, blank=True)
    subid3 = models.CharField(max_length=100, blank=True)
    subtype4 = models.CharField(max_length=50, blank=True)
    subid4 = models.CharField(max_length=100, blank=True)
    subtype5 = models.CharField(max_length=50, blank=True)
    subid5 = models.CharField(max_length=100, blank=True)
    subtype6 = models.CharField(max_length=50, blank=True)
    subid6 = models.CharField(max_length=100, blank=True)
    subtype7 = models.CharField(max_length=50, blank=True)
    subid7 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.display_name, self.id)
    __unicode__ = __str__

    def get_absolute_url(self):
        return reverse('division', args=(self.id,))

    @staticmethod
    def subtypes_from_id(division_id):
        pieces = [piece.split(':', 1) for piece in division_id.split('/')]
        fields = {}

        # if it included the ocd-division bit, pop it off
        if pieces[0] == ['ocd-division']:
            pieces.pop(0)

        if pieces[0][0] != 'country':
            raise ValueError('OCD id must start with country')

        fields['country'] = pieces[0][1]

        # add the remaining pieces
        n = 1
        for stype, subid in pieces[1:]:
            fields['subtype{0}'.format(n)] = stype
            fields['subid{0}'.format(n)] = subid
            n += 1

        return fields, n
