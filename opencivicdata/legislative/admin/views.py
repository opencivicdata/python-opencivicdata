from collections import Counter, defaultdict
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db import models
from django.contrib import messages
from opencivicdata.core.models import Person, PersonName
from ..models import BillSponsorship, PersonVote


def unresolved_legislators(request):
    if request.method == 'POST':
        names = defaultdict(list)
        for name, id in request.POST.items():
            if name == 'csrfmiddlewaretoken':
                continue
            if not id:
                continue
            names[id].append(name)

        people_by_id = Person.objects.in_bulk(names.keys())
        for pid, person in people_by_id.items():
            person.new_names = names[pid]

        people = people_by_id.values()

        return render(request, 'opencivicdata/admin/unresolved-confirm.html',
                      {'people': people}
                      )
    else:
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


@require_POST
def confirm_unresolved_legislators(request):
    if request.POST.get('confirm'):
        for pid, names in request.POST.lists():
            if pid.startswith('ocd-person'):
                for name in names:
                    PersonName.objects.create(person_id=pid, name=name,
                                              note='added via unresolved tool')
                    person = Person.objects.get(pk=pid)
                    if 'other_names' not in person.locked_fields:
                        person.locked_fields.append('other_names')
                        person.save()
                    sp = BillSponsorship.objects.filter(entity_type='person',
                                                        person_id=None, name=name)
                    n_sponsors = sp.update(person_id=pid)
                    vs = PersonVote.objects.filter(voter_id=None, voter_name=name)
                    n_voters = vs.update(voter_id=pid)
                    messages.add_message(request, messages.INFO,
                                         'Updated {} sponsors and {} votes to refer to {}'.format(
                                             n_sponsors, n_voters, pid)
                                         )
        return redirect('unresolved_legislators')
