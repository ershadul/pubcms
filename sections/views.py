# sections views
from django.http import *

from pubcms.lib.paginator import DiggPaginator
from pubcms.articles.models import Article
from pubcms.issues.models import Issue
from pubcms.sections.models import Section
from django.shortcuts import render_to_response

def index(request):
    sections = Section.objects.filter(is_published=True, parent=None).order_by('order').all()

    breadcrumb = []
    breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
            })
    count = len(request.main_menus)
    while count > 0:
        if request.main_menus[count-1]['name'] == 'section':
            request.main_menus[count-1]['is_selected'] = True
            break
        count -= 1

    return render_to_response(request.site.settings.template + '/section_list.html',
        {
            'sections': sections,
            'site': request.site,
            'locals': request.locals,
            'main_menus': request.main_menus,
            'breadcrumb': breadcrumb,
            'top_articles': request.top_articles
        }
    )

def show(request, section_id, page_number='1'):
    ''' '''
    try:
        section = Section.objects.get(pk=section_id)
        article_set = Article.objects.filter(is_published=True, section=section).order_by('-issue__published_at').all()
        if not section.parent:
            related_sections = Section.objects.filter(parent=section).all()
        else:
            related_sections = Section.objects.filter(parent=section.parent).exclude(id=section.id).all()
    except:
        raise Http404

    page = None
    try:
        page_number = int(page_number)
        if page_number < 1:
            raise Exception
    except:
        page_number = 1

    paginator = DiggPaginator(article_set, 10)
    try:
        page = paginator.page(page_number)
        articles = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        articles = page.object_list
    if page:
        page.url = u'%s/' % section.get_absolute_url()

    breadcrumb = []
    breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
            })
    breadcrumb.append({
         'name': request.locals['section'],
         'link': '/section'
        })

    count = len(request.main_menus)
    while count > 0:
        if request.main_menus[count-1]['name'] == 'section':
            request.main_menus[count-1]['is_selected'] = True
            break
        count -= 1

    return render_to_response(request.site.settings.template + '/section.html',
        {
            'section': section,
            'page': page,
            'articles': articles,
            'related_sections': related_sections,
            'site': request.site,
            'locals': request.locals,
            'main_menus': request.main_menus,
            'breadcrumb': breadcrumb,
            'top_articles': request.top_articles
        }
    )

def issue_section(request, issue_date, section_id):
    issue = Issue.objects.get(published_at=issue_date)
    section = Section.objects.get(pk=section_id)
    articles = list(section.article_set.filter(issue=issue, is_published=True).all())
    child_section_articles = list(Article.objects.filter(issue=issue, is_published=True,
        section__in=section.child_sections.filter(is_published=True).order_by('order').all()).all())

    if articles:
        articles[-1].is_last = True
    if child_section_articles:
        child_section_articles[-1].is_last = True
    
    breadcrumb = []
    if issue.is_default:
        link = '/'
    else:
        link = issue.get_absolute_url()
    breadcrumb.append({
             'name': issue.title,
             'link': link
            })
    if section.parent:
        breadcrumb.append(
            {
                'name': '%s' % section.parent.title,
                'link': '%s%s' % (issue.get_absolute_url(), section.parent.get_absolute_url())
            }
    )
    breadcrumb.append(
            {
                'name': '%s' % section.title,
                'link': '%s%s' % (issue.get_absolute_url(), section.get_absolute_url())
            }
    )
    count = len(request.main_menus)
    if issue.is_default:
        while count > 0:
            if request.main_menus[count-1]['name'] == 'current-issue':
                request.main_menus[count-1]['is_selected'] = True
                break
            count -= 1
    else:
        while count > 0:
            if request.main_menus[count-1]['name'] == 'archive':
                request.main_menus[count-1]['is_selected'] = True
                break
            count -= 1
    return render_to_response( request.site.settings.template + '/issue_section.html',
        {
            'articles': articles,
            'child_section_articles': child_section_articles,
            'section': section,
            'issue': issue,
            'site': request.site,
            'locals': request.locals,
            'main_menus': request.main_menus,
            'breadcrumb': breadcrumb
        }
    )
    
    
