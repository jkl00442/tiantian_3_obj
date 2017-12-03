from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^(\d+)/$', views.detail),
    url(r'^has_login/$', views.has_login),
    url(r'^search/?$', views.MySearchView.as_view(), name='search_view'),
]
