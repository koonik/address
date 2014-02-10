from django.conf.urls import patterns, url

from forms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^address/$', views.address, name='address'),
)