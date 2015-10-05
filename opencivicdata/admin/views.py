from collections import Counter
from django.shortcuts import render
from django.db import models
from ..models import BillSponsorship, PersonVote, Person


def unresolved_legislators(request):
    sponsors = BillSponsorship.objects.filter(entity_type='person', person_id=None
                                              ).annotate(num=models.Count('name'))
    voters = PersonVote.objects.filter(voter_id=None).annotate(num=models.Count('voter_name'))

    unresolved = Counter()
    for sp in sponsors:
        unresolved[sp.name] += sp.num
    for v in voters:
        unresolved[v.voter_name] += v.num

    # convert unresolved to a normal dict so it's iterable in template
    unresolved = sorted(((k, v) for (k, v) in unresolved.items()),
                        key=lambda x: x[1], reverse=True)

    people = list(Person.objects.all())

    return render(request, 'opencivicdata/admin/unresolved.html',
                  {'unresolved': unresolved, 'people': people})
