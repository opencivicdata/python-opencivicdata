# Changelog

## 0.9.1

Improvements requiring migrations:

* Add `Membership.person_name` property, allowing unresolved people to be members of Organizations

Improvements:

* Add `amendment-deferral` to match `deferral` and other amendment actions.

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
