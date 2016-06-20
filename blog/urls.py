from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # /
    url(r'^$', views.PostList.as_view(), name='post_list'),
    # /blogs/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail')
]
