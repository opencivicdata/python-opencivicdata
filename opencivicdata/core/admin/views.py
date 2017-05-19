from collections import Counter, defaultdict
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db import models
from django.core import urlresolvers
from django.http import HttpResponseBadRequest
from django.contrib import messages
from ..models import BillSponsorship, PersonVote, Person, PersonName
from ..models.merge import compute_diff, merge


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


def merge_tool(request):
    people = list(Person.objects.all())

    if request.method == 'POST':
        person1 = request.POST['person1']
        person2 = request.POST['person2']

        if person1 == person2:
            messages.add_message(request, messages.ERROR,
                                 'Cannot merge person with themselves.',
                                 )
        person1 = Person.objects.get(pk=person1)
        person2 = Person.objects.get(pk=person2)

        diff = compute_diff(person1, person2)

        return render(request, 'opencivicdata/admin/merge.html',
                      {'people': people,
                       'person1': person1,
                       'person2': person2,
                       'diff': diff,
                       })
    else:
        return render(request, 'opencivicdata/admin/merge.html',
                      {'people': people})


@require_POST
def merge_confirm(request):
    person1 = request.POST['person1']
    person2 = request.POST['person2']
    if person1 == person2:
        return HttpResponseBadRequest('invalid merge!')

    person1 = Person.objects.get(pk=person1)
    person2 = Person.objects.get(pk=person2)

    merge(person1, person2)

    messages.add_message(request, messages.INFO,
                         'merged {} with {}'.format(person1.id, person2.id)
                         )

    return redirect(urlresolvers.reverse('admin:opencivicdata_person_change',
                                         args=(person1.id,))
                    )
