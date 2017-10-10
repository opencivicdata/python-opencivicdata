# Changelog

## WIP

Improvements requiring migrations:

* added missing migration for help_text
* update models to have explicit on_delete settings for Foreign Keys (required by Django 2.0)

## 2.0.0 (2017-07-19)

Backwards-incompatible changes:

* Implementation of [OCDEP #101](http://docs.opencivicdata.org/en/latest/proposals/0101.html) - datetime fields are fuzzy and Event's start/end_time are now start/end_date.

Improvments requiring migrations:

* add extras to BillAction & EventAgendaItem
* add Post.maximum_memberships for validating expected number of memberships, useful for multi-member seats

Improvements:

* jurisdiction specific merge tool
* experimental introduction of opencivicdata.elections - provisional for now w/ future changes likely

Bugfix:

* fix usage of FileNotFoundError on Python 2.7

## 1.0.0 (2017-05-25)

Backwards-incompatible changes:

* This package is renamed to opencivicdata from opencivicdata-divisions and opencivicdata-django.
 This also means it is no longer split into opencivicdata-divisions and opencivicdata-django.  This really shouldn't cause any issues, but you shouldn't be installing opencivicdata-divisions anymore, and doing so explicitly may cause some issues.
* Your requirements.txt or other requirements definition should now use the opencivicdata name exclusively.
* Instead of adding:
    ```'opencivicdata.apps.BaseConfig'`` to your ``INSTALLED_APPS`` you'll need to add:
    ```
    'opencivicdata.core.apps.BaseConfig',
    'opencivicdata.legislative.apps.BaseConfig',
    ```
* If you already have models you'll need to run: ```./manage.py migrate --fake-initial`` to skip the initial migrations for the two new apps.

Improvements requiring migrations:

* Add `Membership.person_name` property, allowing unresolved people to be members of Organizations
* Add `VoteEvent.bill_action`, allowing linking of VoteEvents to bill actions

Improvements:

* Add `amendment-deferral` to match `deferral` and other amendment actions.
* Add `study request` and `concurrent study request` to to bill classifications.
* Basic Python 2.7 support is restored.

## 0.9.0 (2017-02-19)

Backwards-incompatible changes:

* Make bill action classifications consistent:
  * `amendment-amended` is now `amendment-amendment`
  * `committee-referral` is now `referral-committee`
  * `executive-received` is now `executive-receipt`
  * `deferred` is now `deferral`

Improvements requiring migrations:

* Add `EventAgendaItem.classification` property, like Popolo's [Event](http://www.popoloproject.com/specs/event.html) class

Improvements:

* Add `transit_authority` to jurisdiction classifications
* Add `corporation`, `agency`, `department` to organization classifications
* Add `motion` to bill classifications
* Add `receipt`, `referral` to bill action classifications

Fixes:

* Fix `EventRelatedEntity.entity_name` property when the entity is a vote event or bill

## 0.8.2 (2015-11-30)

Fixes:

* Fix package

## 0.8.0 (2015-11-13)

Improvements:

* Add admin views for merging objects

## 0.7.1, 0.7.2, 0.7.3 (2015-10-08/2015-10-12)

Fixes:

* Fix package

## 0.7.0 (2015-10-08)

Backwards-incompatible changes:

* Rename Vote to VoteEvent to align with Popolo's [VoteEvent](http://www.popoloproject.com/specs/vote-event.html) class, #27

Improvements:

* Various improvements to admin views
* Add admin views for unresolved people
* Add `Organization.get_current_members` method
* Add `text` field to `MimetypeLinkBase` abstract class
* Upgrade Django from 1.8 to 1.9 and remove `djorm-ext-pgarray`, `jsonfield`, `django-uuidfield` dependencies

Fixes:

* Fix package.

## 0.6.4 (2015-08-30)

Start of changelog
