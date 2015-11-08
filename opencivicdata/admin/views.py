import datetime
from collections import Counter, defaultdict
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db import models
from django.contrib import messages
from ..models import BillSponsorship, PersonVote, Person, PersonName


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


def _compute_diff(obj1, obj2):
    comparison = []
    fields = obj1._meta.get_fields()
    exclude = ('created_at', 'updated_at', 'id')

    # diff is either one, two, or new

    for field in fields:
        if field.name in exclude:
            continue
        elif not field.is_relation:
            piece_one = getattr(obj1, field.name)
            piece_two = getattr(obj2, field.name)
            comparison.append({
                'field': field.name,
                'new': getattr(obj1, field.name),
                'one': getattr(obj1, field.name),
                'two': getattr(obj2, field.name),
                'diff': 'none' if piece_one == piece_two else 'one',
            })
        elif field.related_name:
            piece_one = list(getattr(obj1, field.related_name).all())
            piece_two = list(getattr(obj2, field.related_name).all())
            comparison.append({
                'field': field.name,
                # TODO: try and deduplicate the lists?
                'new': piece_one + piece_two,
                'one': getattr(obj1, field.related_name).all(),
                'two': getattr(obj2, field.related_name).all(),
                'diff': 'none' if piece_one == piece_two else 'one',
                'list': True,
            })
        else:
            # TODO: resolve these
            print(field.name, field.related_name)

    comparison.append({'field': 'created_at',
                       'new': min(obj1.created_at, obj2.created_at),
                       'one': obj1.created_at,
                       'two': obj2.created_at,
                       'diff': 'one' if obj1.created_at < obj2.created_at else 'two',
                       })
    comparison.append({'field': 'updated_at',
                       'new': datetime.datetime.now(),
                       'one': obj1.updated_at,
                       'two': obj2.updated_at,
                       'diff': 'new',
                       })
    return comparison


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

        diff = _compute_diff(person1, person2)

        return render(request, 'opencivicdata/admin/merge.html',
                      {'people': people,
                       'person1': person1,
                       'person2': person2,
                       'diff': diff,
                       })
    else:
        return render(request, 'opencivicdata/admin/merge.html',
                      {'people': people})
