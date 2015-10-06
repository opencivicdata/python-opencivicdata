from django.conf.urls import url

urlpatterns = [
    url(r'^opencivicdata/unresolved/$',
        'opencivicdata.admin.views.unresolved_legislators',
        name='unresolved_legislators'),
    url(r'^opencivicdata/unresolved/confirm/$',
        'opencivicdata.admin.views.confirm_unresolved_legislators',
        name='confirm_unresolved_legislators'),
]
