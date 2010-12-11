from django.conf.urls.defaults import *
from django.conf import settings


#from django.contrib import admin
#admin.autodiscover()

handler404 = 'pubcms.views.show_404'
handler500 = 'pubcms.views.show_500'

urlpatterns = patterns('',
    #(r'^admin/', include(admin.site.urls)),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
    (r'^issue/(?P<issue_date>[0-9\-]+)/article/', include('pubcms.articles.urls')),
    (r'^issue/(?P<issue_date>[0-9\-]+)/section/', include('pubcms.sections.urls')),
    (r'^section$', 'pubcms.sections.views.index'),
    (r'^section/(?P<section_id>\d+)$', 'pubcms.sections.views.show'),
    (r'^section/(?P<section_id>\d+)/(?P<page_number>\d+)', 'pubcms.sections.views.show'),
    (r'^about$', 'pubcms.views.about'),
    (r'^contact$', 'pubcms.views.contact'),
    (r'^feedback$', 'pubcms.feedbacks.views.feedback'),
    (r'^search', 'pubcms.views.search'),
    (r'^help/font', 'pubcms.views.font_help'),
    (r'^robots\.txt$', 'pubcms.views.robots'),
    (r'^', include('pubcms.issues.urls')),

)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
        ) + urlpatterns
