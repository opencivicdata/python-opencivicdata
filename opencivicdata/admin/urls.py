from django.conf.urls import url

urlpatterns = [
    url(r'^opencivicdata/unresolved/$',
        'opencivicdata.admin.views.unresolved_legislators'),
]
