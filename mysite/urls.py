from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^forms/', include('forms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
