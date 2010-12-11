from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('pubcms.articles.views',
    (r'^(?P<article_id>\d+)/print', 'show_printable_version'),
    (r'^(?P<article_id>\d+)/(?P<service>\w+)', 'share'),
    (r'^(?P<article_id>\d+)', 'show'),
)