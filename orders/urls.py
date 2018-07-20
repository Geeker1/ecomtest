from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^success/$', views.success_me, name='success_me'),
]

