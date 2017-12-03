from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^order_handle/$', views.order_handle),
]
