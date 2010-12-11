from django.http import HttpResponsePermanentRedirect
from pubcms.lib import locals
from pubcms.articles.models import Article

class DomainMiddleware:
    """ Set subdomain attribute to request object. """
    
    def process_request(self, request):
        """Parse out the subdomain from the request"""
        subdomain = ''
        domain = ''
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        if len(host_s) > 2:
            subdomain = ''.join(host_s[:-2])
            domain = '.'.join(host_s[1:])
        else:
            domain = host
        
        if subdomain == 'admin':
           setattr(request, 'urlconf', 'pubcms.admin_urls')
        
        setattr(request, 'domain', domain)
        setattr(request, 'subdomain', subdomain)
        
        return None

class PubCMSMiddleware(object):
    def process_request(self, request):
        request.locals = locals.locals
        request.main_menus = locals.get_main_menu()
        request.top_articles = Article.objects.filter(is_published=True).order_by('-n_clicks').all()