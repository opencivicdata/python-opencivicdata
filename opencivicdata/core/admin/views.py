from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core import urlresolvers
from django.http import HttpResponseBadRequest
from django.contrib import messages
from ..models import Person
from ...merge import compute_diff, merge
from opencivicdata.core.models import Jurisdiction


def merge_tool(request, jur_id):
    people = Person.objects \
        .filter(memberships__organization__jurisdiction__id=jur_id) \
        .distinct()
    jur_name = Jurisdiction.objects.get(id=jur_id).name
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
                       'jur_name': jur_name,
                       })
    else:
        return render(request, 'opencivicdata/admin/merge.html',
                      {'people': people, 'jur_name': jur_name})


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

    return redirect(urlresolvers.reverse('admin:core_person_change',
                                         args=(person1.id,))
                    )
