from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^opencivicdata/(?P<jur_id>.*)/merge/$', views.merge_tool,
        name='merge'),
    url(r'^opencivicdata/merge/confirm/$', views.merge_confirm,
        name='merge_confirm'),
]
