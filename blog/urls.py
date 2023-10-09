from django.urls import include, re_path
# from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]