from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.index import index   
from view.upload import upload

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vipsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^upload/',upload , ),
)
