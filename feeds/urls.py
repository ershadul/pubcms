from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^rss/current$', 'pubcms.feeds.views.rss'),
)
