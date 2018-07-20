from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^contact_save/$',
    views.contact_save,
    name='contact_save'),
    
]