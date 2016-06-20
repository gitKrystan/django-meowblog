from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # /
    url(r'^$', views.PostList.as_view(), name='post_list'),
    # /blogs/5/
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail')
]
