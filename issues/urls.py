from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('pubcms.issues.views',
    (r'^archive$', 'archive'),
    (r'^issue/(?P<issue_date>[0-9\-]+)$', 'index'),
    (r'^$', 'index'),
)