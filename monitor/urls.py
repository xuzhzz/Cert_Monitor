from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^cert$', views.create_monitor),
    url(r'^detail$', views.certs_detail),
]