from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/(?P<contactId>[0-9]+)/$', views.update, name='update'),
    url(r'^delete/(?P<contactId>[0-9]+)/$', views.delete, name='delete'),
]
