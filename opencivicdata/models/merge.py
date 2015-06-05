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
        old_field = new_dict.pop(f)
        if old_field:
            setattr(persistent_obj, f, old_field)

    for f in keep_new:
        new_field = new_dict.pop(f)
        if new_field:
            setattr(persistent_obj, f, new_field)
    for f in custom_fields:
        new_dict.pop(f)

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



def start_and_end_dates(old, new, persistent, keep_old=[], keep_new=[],
                        custom_fields=[], force=False):

    # if the objects overlap, take the earlier start date and later end date
    # if dates are missing, fill in the valid date
    # if the objects do not overlap, only merge if forced.
    # deal with missing

    if not new.start_date and not new.end_date:
        keep_old.append('start_date')
        keep_old.append('end_date')

    elif not new.start_date:
        keep_old.append('start_date')
        setattr(persistent, 'end_date', max(old.end_date, new.end_date))
        custom_fields.append('start_date')

    elif not new.end_date:
        keep_old.append('end_date')
        setattr(persistent, 'start_date', min(old.start_date, new.start_date))
        custom_fields.append('start_date')

    elif not old.start_date and not old.end_date:
        keep_new.append('start_date')
        keep_new.append('end_date')

    elif not old.start_date:
        keep_new.append('start_date')
        setattr(persistent, 'end_date', max(old.end_date, new.end_date))
        custom_fields.append('start_date')

    elif not old.end_date:
        keep_new.append('end_date')
        setattr(persistent, 'start_date', min(old.start_date, new.start_date))
        custom_fields.append('start_date')

    elif new.start_date <= old.start_date <= new.end_date <= old.end_date:
        setattr(persistent, 'start_date', new.start_date)
        custom_fields.extend(['start_date', 'end_date'])

    elif new.start_date <= old.start_date <= old.end_date <= new.end_date:
        setattr(persistent, 'start_date', new.start_date)
        setattr(persistent, 'end_date', new.end_date)
        custom_fields.extend(['start_date', 'end_date'])

    elif old.start_date <= new.start_date <= old.end_date <= new.end_date:
        setattr(persistent, 'end_date', new.end_date)
        custom_fields.extend(['start_date', 'end_date'])

    elif old.start_date <= new.start_date <= new.end_date <= old.end_date:
        custom_fields.extend(['start_date', 'end_date'])

    elif force:
        # ug, this is really terrible, we're merging two memberships
        # that don't overlap with each other. We're setting the dates
        # to the outer bounds for now but maybe we should set to None instead?
        setattr(persistent, 'start_date', min(old.start_date, new.start_date))
        setattr(persistent, 'end_date', max(old.end_date, new.end_date))
        custom_fields.extend(['start_date', 'end_date'])

    else:
        msg = "Time ranges do not overlap, will not merge "\
              "unless forced. Please do not do this unless you "\
              "are ABSOLUTELY sure you know what you're doing. "\
              "You've been warned."
        raise AssertionError(msg)

    return (keep_old, keep_new, custom_fields)


def set_up_merge(obj1, obj2, obj_type):

    assert (obj1.__class__.__name__ == obj_type and
            obj2.__class__.__name__ == obj_type), \
        "{0} merger needs two {0} objects".format(obj_type)

    # determine which was updated most recently
    if obj1.updated_at > obj2.updated_at:
        return obj1, obj2
    return obj2, obj1
