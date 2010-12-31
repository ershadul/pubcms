# -*- coding: utf-8 -*-

from django.http import *
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.feedgenerator import Atom1Feed

from pubcms.issues.models import Issue

def rss(request, issue=None):
    try:
        issue = Issue.objects.filter(is_default=True,
            is_published=True).all()[0:1].get()
    except:
        raise Http404
    
    articles = issue.article_set.filter(is_published=True).order_by('order').all()
    
    feed = Rss201rev2Feed(title=request.site.name + u' - ' + issue.title, 
        link=u'http:/www.alqualam.com',
        feed_url=u'http://' + request.get_host() + request.get_full_path(),
        description=request.site.settings.slogan
    )
    
    for article in articles:
        if article.intro_text:
            description = article.intro_text
        else:
            description = article.get_title()
        
        feed.add_item(title=article.get_title(),
            link=u'http://' + request.get_host() + article.get_absolute_url(),
            description=description,
            pubdate=article.created_at
        )
    return HttpResponse(feed.writeString('UTF-8'), mimetype='application/rss+xml')

    
