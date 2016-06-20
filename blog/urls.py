from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # /blogs/
    url(r'^$', views.ListView.as_view(), name='list'),
    # /blogs/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail')
]
