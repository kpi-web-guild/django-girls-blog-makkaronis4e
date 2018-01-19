"""Django based blog URL mapping."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/new/$', views.NewPost.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.EditPost.as_view(), name='post_edit'),
]
