import datetime
from django.db import transaction


def compute_diff(obj1, obj2):
    """
        Given two objects compute a list of differences.

        Each diff dict has the following keys:
            field - name of the field
            new - the new value for the field
            one - value of the field in obj1
            two - value of the field in obj2
            diff - none|one|two|new
            list - true if field is a list of related objects
    """
    comparison = []
    fields = obj1._meta.get_fields()
    exclude = ('created_at', 'updated_at', 'id', 'locked_fields')

    if obj1 == obj2:
        raise ValueError('cannot merge object with itself')

    for field in fields:
        if field.name in exclude:
            continue
        elif not field.is_relation:
            piece_one = getattr(obj1, field.name)
            piece_two = getattr(obj2, field.name)
            if piece_one == piece_two:
                diff = 'none'
                new = piece_one
            elif piece_one:
                diff = 'one'
                new = piece_one
            elif piece_two:
                diff = 'two'
                new = piece_two
            comparison.append({
                'field': field.name,
                'new': new,
                'one': getattr(obj1, field.name),
                'two': getattr(obj2, field.name),
                'diff': diff,
                'list': False,
            })
        else:
            related_name = field.get_accessor_name()
            piece_one = list(getattr(obj1, related_name).all())
            piece_two = list(getattr(obj2, related_name).all())
            # TODO: try and deduplicate the lists?
            new = piece_one + piece_two
            diff = 'none' if piece_one == piece_two else 'one'

            if (field.name == 'other_names' and obj1.name != obj2.name):
                new.append(field.related_model(name=obj2.name,
                                               note='from merge w/ ' + obj2.id)
                           )
                diff = 'new'
            if field.name == 'identifiers':
                new.append(field.related_model(identifier=obj2.id))
                diff = 'new'
            if field.name == 'memberships':
                new = _dedupe_memberships(new)

            comparison.append({
                'field': related_name,
                'new': new,
                'one': piece_one,
                'two': piece_two,
                'diff': diff,
                'list': True,
            })

    comparison.append({'field': 'created_at',
                       'new': min(obj1.created_at, obj2.created_at),
                       'one': obj1.created_at,
                       'two': obj2.created_at,
                       'diff': 'one' if obj1.created_at < obj2.created_at else 'two',
                       'list': False,
                       })
    comparison.append({'field': 'updated_at',
                       'new': datetime.datetime.utcnow(),
                       'one': obj1.updated_at,
                       'two': obj2.updated_at,
                       'diff': 'new',
                       'list': False,
                       })
    # locked fields are any fields that change that aren't M2M relations
    # (ending in _set)
    new_locked_fields = obj1.locked_fields + obj2.locked_fields + [
        c['field'] for c in comparison if c['diff'] != 'none' and not c['field'].endswith('_set')
    ]
    new_locked_fields = set(new_locked_fields) - {'updated_at', 'created_at'}
    comparison.append({'field': 'locked_fields',
                       'new': list(new_locked_fields),
                       'one': obj1.locked_fields,
                       'two': obj2.updated_at,
                       'diff': 'new',
                       'list': False,
                       })

    return comparison


@transaction.atomic
def apply_diff(obj1, obj2, diff):
    for row in diff:
        if row['diff'] != 'none':
            if row['list']:
                # save items, the ids have been set to obj1
                for item in row['new']:
                    setattr(item,
                            getattr(obj1, row['field']).field.name,
                            obj1)
                    item.save()
            else:
                setattr(obj1, row['field'], row['new'])

    obj1.save()
    count, delete_plan = obj2.delete()
    if count > 1:
        # shouldn't happen, but let's be sure
        raise AssertionError('deletion failed due to related objects left unmerged')


def merge(obj1, obj2):
    diff = compute_diff(obj1, obj2)
    apply_diff(obj1, obj2, diff)


def _dedupe_memberships(memberships):
    deduped = []
    mset = set()
    for membership in memberships:
        mkey = (membership.organization_id,
                membership.label,
                membership.end_date,
                membership.post_id)
        if mkey not in mset:
            deduped.append(membership)
            mset.add(mkey)
        else:
            membership.delete()
    return deduped
