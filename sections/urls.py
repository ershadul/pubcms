from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('pubcms.sections.views',
    (r'^(?P<section_id>\d+)$', 'issue_section'),
    (r'^$', 'index'),
)