from django.conf.urls import url
import views

urlpatterns = [
    url(r'^add_cart/$', views.add_cart),
    url(r'^cart_show/$', views.cart_show),
    url(r'^$', views.index),
    url(r'^edit/$', views.edit),
    url(r'^delete_cart/$', views.delete_cart),
]
