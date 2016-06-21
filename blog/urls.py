from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # /
    url(r'^$', views.PostList.as_view(), name='post_list'),
    # /posts/5/
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    # /posts/new/
    url(r'^posts/new/$', views.PostCreate.as_view(), name='post_create'),
]
