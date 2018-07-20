from django.contrib import admin
from django.conf.urls import url, static,include
from . import views

urlpatterns = [
    url(r'^$', views.emailView, name='email'),
    url(r'^success/$', views.successView, name='success'),
]