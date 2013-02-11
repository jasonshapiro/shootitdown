from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from shootitdown_app.views import *
from django.conf.urls.defaults import *
admin.autodiscover()

# And include this URLpattern...
urlpatterns = patterns('',
    ('^$', current_datetime),
    (r'^submit/', submit),
    (r'^latest/', latest),
    (r'^admin/', include(admin.site.urls)),
)
