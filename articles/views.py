# article views
import urllib
from django.http import *

from pubcms.articles.models import Article
from django.shortcuts import render_to_response

def show(request, issue_date, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.n_clicks += 1
        article.save()
        related_articles = []
        if article.section:
            related_articles = article.section.article_set.filter(is_published=True).exclude( \
                id=article.id).order_by('-issue__published_at').all()[:15]
    except:
        raise Http404
    if article.issue.is_default:
        link = '/'
    else:
        link = article.issue.get_absolute_url()

    breadcrumb = []
    breadcrumb.append({
             'name': article.issue.title,
             'link': link
            })
    if article.section and article.section.parent:
        breadcrumb.append(
            {
                'name': u'%s' % article.section.parent.title,
                'link': u'%s%s' % (article.issue.get_absolute_url(), article.section.parent.get_absolute_url())
            }
    )
    if article.section:
        breadcrumb.append(
            {
                'name': u'%s' % article.section.title,
                'link': u'%s%s' % (article.issue.get_absolute_url(), article.section.get_absolute_url())
            }
        )

    menus = request.main_menus
    for menu in menus:
        if article.issue.is_default:
            if menu['name'] == 'current-issue':
                menu['is_selected'] = True
                break
        else:
            if menu['name'] == 'archive':
                menu['is_selected'] = True
                break
    return render_to_response(request.site.settings.template + '/article.html',
        {
            'article': article,
            'related_articles': related_articles,
            'issue': article.issue,
            'site': request.site,
            'locals': request.locals,
            'main_menus': menus,
            'breadcrumb': breadcrumb
        })


def show_printable_version(request, issue_date, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except:
        raise Http404

    return render_to_response(request.site.settings.template + '/article_print.html',
        {
            'article': article,
            'site': request.site,
            'locals': request.locals
        })

def share(request, issue_date, article_id, service):
    try:
        article = Article.objects.get(pk=article_id)
    except:
        raise Http404

    parameters = {}
    if service == 'twitter':
        parameters['status'] = u'%s' % (article.get_absolute_url())
        return HttpResponseRedirect('http://www.twitter.com/home?' + urllib.urlencode(parameters))
        
    return HttpResponse(service)
