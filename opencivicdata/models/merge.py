from waterfall import CascadingUpdate



def common_merge(persistent_obj, obsolete_obj,
          new, old, keep_new, keep_old, custom_fields, force=False):

    #persistent/obsolete and new/old are two sets of pointers
    #to the same object. We need to do this so we can both
    #persist the desired object and transfer newer fields
    #whether the persistent object is the newer or older.
    #ick. but better than alternatives.

    # TODO: check for human_edited fields
    # do stuff that is common to everything
    

    # if we add fields to the model, we catch it here
    new_dict = new.__dict__.copy()
    new_dict.pop('id')
    for f in keep_old:
        if f in new.locked_fields and f not in old.locked_fields:
            field_val = getattr(new, f)
        else:
            field_val = getattr(old, f)
        new_dict.pop(f)
        if field_val:
            setattr(persistent_obj, f, field_val)

    for f in keep_new:
        field_val = new_dict.pop(f)
        if f in old.locked_fields and f not in new.locked_fields:
            field_val = getattr(old, f)
        if field_val:
            setattr(persistent_obj, f, field_val)
    for f in custom_fields:
        new_dict.pop(f)

    for f in obsolete_obj.locked_fields:
        if f not in persistent_obj.locked_fields:
            persistent_obj.locked_fields.append(f)

    new_dict.pop('locked_fields')

    setattr(persistent_obj, "created_at", min(old.created_at, new.created_at))
    new_dict.pop('created_at')
    new_dict.pop('updated_at')
    bad_keys = []
    for k in new_dict:
        if k.startswith("_"):
            bad_keys.append(k)
    for k in bad_keys:
        new_dict.pop(k)

    assert len(new_dict) == 0, \
        "Unexpected fields found: {}".format(', '.join(new_dict.keys()))

    # update foreign keys
    c = CascadingUpdate()
    c.merge_foreign_keys(obsolete_obj, persistent_obj)

    # save old, delete new
    persistent_obj.save()
    obsolete_obj.delete()

    return persistent_obj



def start_and_end_dates(persistent_obj, obsolete_obj, keep_old=[], keep_new=[],
                        custom_fields=[], force=False):
    if not force:
        if ((persistent_obj.end_date and obsolete_obj.start_date
            and persistent_obj.end_date < obsolete_obj.start_date)
            or (obsolete_obj.end_date and persistent_obj.start_date
            and obsolete_obj.end_date < persistent_obj.start_date)):

                msg = "Time ranges do not overlap, will not merge "\
                      "unless forced. Please do not do this unless you "\
                      "are ABSOLUTELY sure you know what you're doing. "\
                      "You've been warned."
                raise AssertionError(msg)

    start_date = (min(persistent_obj.start_date, obsolete_obj.start_date)
                  or persistent_obj.start_date or obsolete_obj.start_date)
    end_date = max(persistent_obj.end_date, obsolete_obj.end_date)
    setattr(persistent_obj, 'start_date', start_date)
    setattr(persistent_obj, 'end_date', end_date)

    return (keep_old, keep_new, ['start_date', 'end_date'])


def set_up_merge(obj1, obj2, obj_type):

    assert (obj1.__class__.__name__ == obj_type and
            obj2.__class__.__name__ == obj_type), \
        "{0} merger needs two {0} objects".format(obj_type)

    # determine which was updated most recently
    if obj1.updated_at > obj2.updated_at:
        return obj1, obj2
    return obj2, obj1
