# pubcms/views

from django.http import *
from django.shortcuts import *

from pubcms.articles.models import Article
from pubcms.lib.paginator import DiggPaginator

def about(request):
    menus = request.main_menus
    selected_menu = None
    for m in menus:
        if m['name'] == 'about':
            m['is_selected'] = True
            selected_menu = m
            break
    if not selected_menu:
        raise Http404
    
    breadcrumb = []
    breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
            })
    breadcrumb.append(
            {
                'name': selected_menu['title'],
                'link': '#'
            }
    )
    #top_articles = Article.objects.filter(is_published=True).order_by('-n_clicks').all()
    return render_to_response(request.site.settings.template + '/about.html',
        {
            'site': request.site,
            'breadcrumb': breadcrumb,
            'selected_menu': selected_menu,
            'main_menus': request.main_menus,
            'locals': request.locals,
            'top_articles': request.top_articles
        })

def contact(request):
    menus = []
    menus = request.main_menus
    selected_menu = None
    for m in menus:
        if m['name'] == 'contact':
            m['is_selected'] = True
            selected_menu = m
            break
    
    if not selected_menu:
        raise Http404

    breadcrumb = []
    breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
            })
    breadcrumb.append(
            {
                'name': selected_menu['title'],
                'link': '#'
            }
    )
    return render_to_response(request.site.settings.template + '/contact.html',
        {
            'site': request.site,
            'breadcrumb': breadcrumb,
            'selected_menu': selected_menu,
            'main_menus': request.main_menus,
            'locals': request.locals,
            'top_articles': request.top_articles
        })

def post_article(request):
    menus = []
    menus = request.main_menus
    selected_menu = None
    for m in menus:
        if m['name'] == 'post_article':
            m['is_selected'] = True
            selected_menu = m
            break

    if not selected_menu:
        raise Http404

    breadcrumb = []
    breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
            })
    breadcrumb.append(
            {
                'name': selected_menu['title'],
                'link': '#'
            }
    )
    return render_to_response(request.site.settings.template + '/post_article.html',
        {
            'site': request.site,
            'breadcrumb': breadcrumb,
            'selected_menu': selected_menu,
            'main_menus': request.main_menus,
            'locals': request.locals,
            'top_articles': request.top_articles
        })

def search(request):
    query =  request.GET.get('query', '')
    if query:
        q = u'%' + query + u'%'
        articles_set =  Article.objects.filter(is_published=True).extra( \
            where=[' title LIKE %s or body_text LIKE %s '], params=[q, q]).all()
    else:
        articles_set = []

    page = None
    try:
        page_number = int(request.GET.get('page', '1'))
        page_number = int(page_number)
        if page_number < 1:
            raise Exception
    except:
        page_number = 1

    paginator = DiggPaginator(articles_set, 10)
    try:
        page = paginator.page(page_number)
        articles = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        articles = page.object_list
    if page:
        page.url = u'/search?query=%s&page=' % query
    return render_to_response(request.site.settings.template + '/search.html', {
        'site': request.site,
        'locals': request.locals,
        'articles': articles,
        'page': page,
        'query': query,
        'main_menus': request.main_menus,
        'top_articles': request.top_articles
    })


def font_help(request):
    return render_to_response(request.site.settings.template + '/font_help.html', {
        'site': request.site,
        'locals': request.locals,
        'main_menus': request.main_menus,
        'top_articles': request.top_articles
    })

def robots(request):
    return render_to_response(request.site.settings.template + '/robots.html', {
        'site': request.site
    }, mimetype="text")


def show_404(request):
    return render_to_response('404.html')

def show_500(request):
    return render_to_response('500.html')