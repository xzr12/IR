from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
	url(r'^home/$', 'wordCorrection.views.home', name='home'),
	url(r'^search/$', 'wordCorrection.views.search', name='search'),
	url(r'^noCorrectSearch/(?P<input>.+)$', 'wordCorrection.views.searchNoCorrect', name='searchNoCorrect'),
    # url(r'^calc/tf/$', 'wordCorrection.views.getTf', name='getTf'),
    # url(r'^calc/idf/$', 'wordCorrection.views.getIdf', name='getIdf'),
    # url(r'^test/$', 'wordCorrection.views.test', name='test'),
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
