from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^opencivicdata/unresolved/$', views.unresolved_legislators,
        name='unresolved_legislators'),
    url(r'^opencivicdata/unresolved/confirm/$', views.confirm_unresolved_legislators,
        name='confirm_unresolved_legislators'),
]
