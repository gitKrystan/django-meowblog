from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # /blogs/
    url(r'^$', views.list, name='list'),
]
