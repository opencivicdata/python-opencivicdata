from .. import models
from django.db import connection
from waterfall import CascadingUpdate

def merge_people(obj1, obj2, force=False):
    #if force is true, we'll merge even if sanity checks fail
    new, old = self.set_up_merge(obj1, obj2, "Person")
    
    keep_old = []
    keep_new = ['sort_name' 'family_name',
                'given_name', 'image', 'gender', 'summary',
                'national_identity', 'biography',
                'death_date']

    #fields that require something more complicated:
    #name (add to other names)
    #birth_date (if they don't match, only merge if force=True)

    #TODO: check for human_edited fields

    new_birthday = new.pop('birth_date')
    if old.birth_date != ''
        and new_birthday != ''
        and old.birth_date != new_birthday
        and not force:
            raise AssertionError("Refusing to merge people with different birthdays.")
    
    if new_birthday:
        #we'll only get here if old.birth_date is empty
        setattr(old, "birth_date", new_birthday)

    new_dict = new.__dict__
    new_dict.pop('id')
    for f in keep_old:
        new_dict.pop(f)
    for f in keep_new:
        new_field = new_dict.pop(f)
        if new_field:
            #if new doesn't have a value, keep old.
            setattr(old, f, new_field)

    #TODO: uncomment when uuid gets fixed
    '''
    if old.name not in old.other_names:
        old.add_other_name(old.name)
    if new_fields.name not in old.other_names:
        old.add_other_name(new_dict.name)

    for n in new.other_names:
        old.other_names.add(n)
    '''

    old.name = new_dict.pop('name')

    #if we add fields to the model, we catch it here
    assert len(new_dict) == 0, \
        "Unexpected fields found: {}".format(', '.join(new_dict.keys()))


    self.combine_contact_details(old, new)
    self.combine_identifiers(old, new)
    self.combine_links(old, new, "links")
    self.combine_links(old, new, "sources")


    #memberships

    #if a membership with the same post and org exists in old:
        #if one is a subset of the other, use the superset
        #if one extends the other in either direction, modify old's start or end
        #(possible the above 2 could be done in a merge_memberships method)
        #if they don't overlap, keep them both

    #else transfer the new membership to old

    """
    #update foreign keys
    c = CascadingUpdate()
    c.merge_foreign_keys(new, old)

    #save old, delete new    
    old.save()
    new.delete()
    """

def combine_contact_details(self, old, new):
    #add new's contact details to old
    #unless one exists with the same type and value
    for contact in new.contact_details:
        old_matches = old.contact_details.filter(type=contact.type,
                        value=contact.value)
        if len old_matches == 0:
            old.contact_details.add(contact)

def combine_identifiers(self, old, new):
    #add new's identifiers to old unless one exists
    #with the same identifier and scheme
    for i in new.identifiers:
        old_matches = old.identifiers.filter(identifier = i.identifier,
                                scheme = i.scheme)
        if len(old_matches) == 0:
            old.identifiers.add(i)

def combine_links(self, old, new, link_name="links"):
    #link_name is the related_name for the link we want to merge
    for l in getattr(new, link_name):
        old_matches = getattr(old, links_name).filter(url=l.url)
        if len(old_matches) == 0:
            getattr(old, links_name).add(l)


def merge_memberships(self, obj1, obj2, force=False):
    #assuming we've already decided we want to merge them
    #we this will generally be called from person or post
    #and we should probably do some careful checking there
    #to make sure we want to merge not reassign

    #this will still fail if the memberships are noncontiguous
    #for example, a membership with end date 2013-01-13 and
    #another with start date 2015-01-13 will fail unless force=True

    new, old = self.set_up_merge(obj1, obj2, 'Membership')
    



def set_up_merge(self, obj1, obj2, obj_type):
    assert (obj1.__class__.__name__ == obj_type, \
            obj2.__class__.__name__ == obj_type) \
            "{0} merger needs two {0} objects".format(obj_type)

    #determine which was updated most recently
    if obj1.updated_at > obj2.updated_at:
        return obj1, obj2
    return obj2, obj1
