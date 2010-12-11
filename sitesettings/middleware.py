from django.contrib.sites.models import Site
from django.conf import settings

class SiteMiddleware(object):
    def process_request(self, request):
        request.site = Site.objects.get(pk=settings.SITE_ID)