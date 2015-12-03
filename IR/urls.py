from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^testMongo/$', 'testMongo.views.index'),
	url(r'^testMongo/(?P<key_id>\d+)/(?P<value_id>\d+)/$', 'testMongo.views.saveData'),
	url(r'^testMongo/(?P<key_id>\d+)/$', 'testMongo.views.readData'),

    # Examples:
    # url(r'^$', 'IR.views.home', name='home'),
    # url(r'^IR/', include('IR.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
