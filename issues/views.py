# issues/views

from django.http import *
from django.shortcuts import *

from pubcms.issues.models import Issue, IssueSectionAssociation
from pubcms.sections.models import Section
from pubcms.articles.models  import Article

def index_old(request, issue_date=''):
    try:
        if not issue_date:
            issue = Issue.objects.filter(is_default=True, is_published=True).all()[0:1].get()
        else:
            issue = Issue.objects.get(published_at=issue_date)
    except Exception, e:
        raise Http404
    
    temp_articles = list(issue.article_set.filter(is_published=True).order_by('order').all())
    articles = []
    for a in temp_articles:
        if a.section:
            if a.section.parent:
                if a.section.parent.is_published:
                    articles.append( a )
            else:
                if a.section.is_published:
                    articles.append( a )
        else:
            articles.append( a )
    

    section_ids = []
    for article in articles:
        if article.section_id not in section_ids:
            section_ids.append(article.section_id)

    sections = list(Section.objects.filter(is_published=True).order_by('order').all())
    section_id_dict = {}
    index = 0
    for section in sections:
        section.articles = []
        section_id_dict[section.id] = index
        index += 1

    for article in articles:
        if article.section_id:
            sec = sections[section_id_dict[article.section_id]]
            sec.articles.append(article)

    parent_sections = []
    for section in sections:
        if not section.parent:
            section.sub_sections = []
            for s in sections:
                if s.articles and section == s.parent:
                    section.sub_sections.append(s)
            parent_sections.append(section)

    index = 0
    left_sections = []
    right_sections = []
    for s in parent_sections:
        if index % 2 == 0:
            left_sections.append(s)
        else:
            right_sections.append(s)
        index += 1

    if left_sections:
        left_sections[0].is_first = True
    if right_sections:
        right_sections[0].is_first = True

    menus = request.main_menus
    for menu in menus:
        if issue.is_default:
            if menu['name'] == 'current-issue':
                menu['is_selected'] = True
            else:
                menu['is_selected'] = False
        else:
            if menu['name'] == 'archive':
                menu['is_selected'] = True
            else:
                menu['is_selected'] = False
            
    request.main_menus = menus

    breadcrumb = []
    if not issue.is_default:
        breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
        })
        breadcrumb.append({
            'name': request.locals['archive'],
            'link': '/archive'
        })

    top_articles = Article.objects.filter(is_published=True).order_by('-n_clicks').all()
    
    return render_to_response(request.site.settings.template + '/index.html', {
        'articles': articles,
        'top_articles': top_articles,
        #'left_articles': left_articles,
        #'right_articles': right_articles,
        'sections': sections,
        'left_sections': left_sections,
        'right_sections': right_sections,
        'issue': issue,
        'site': request.site,
        'locals': request.locals,
        'main_menus': request.main_menus,
        'breadcrumb': breadcrumb
    })

def index(request, issue_date=''):
    try:
        if not issue_date:
            issue = Issue.objects.filter(is_default=True, is_published=True).all()[0:1].get()
        else:
            issue = Issue.objects.get(published_at=issue_date)
    except Exception, e:
        raise Http404

    articles = []
    issue_sections = IssueSectionAssociation.objects.filter(issue=issue).order_by('order').all()
    sections = []
    for issue_section in issue_sections:
        section = issue_section.section
        section.articles = issue_section.section.article_set.filter(is_published=True, issue=issue).order_by('order').all()
        sections.append(section)
    index = 1
    left_sections = []
    right_sections = []
    for s in sections:
        if index % 2 != 0:
            left_sections.append(s)
        else:
            right_sections.append(s)
        index += 1

    if left_sections:
        left_sections[0].is_first = True
    if right_sections:
        right_sections[0].is_first = True

    menus = request.main_menus
    for menu in menus:
        if issue.is_default:
            if menu['name'] == 'current-issue':
                menu['is_selected'] = True
            else:
                menu['is_selected'] = False
        else:
            if menu['name'] == 'archive':
                menu['is_selected'] = True
            else:
                menu['is_selected'] = False

    request.main_menus = menus

    breadcrumb = []
    if not issue.is_default:
        breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
        })
        breadcrumb.append({
            'name': request.locals['archive'],
            'link': '/archive'
        })

    top_articles = Article.objects.filter(is_published=True).order_by('-n_clicks').all()

    return render_to_response(request.site.settings.template + '/index.html', {
        'articles': articles,
        'top_articles': top_articles,
        #'left_articles': left_articles,
        #'right_articles': right_articles,
        'sections': sections,
        'left_sections': left_sections,
        'right_sections': right_sections,
        'issue': issue,
        'site': request.site,
        'locals': request.locals,
        'main_menus': request.main_menus,
        'breadcrumb': breadcrumb
    })

def archive(request):
    issues = Issue.objects.filter(is_published=True, is_default=False).all()
    selected_menu = None
    menus = request.main_menus
    for menu in menus:
        if menu['name'] == 'archive':
            selected_menu = menu
            menu['is_selected'] = True
            break
    request.main_menus = menus

    breadcrumb = []
    breadcrumb.append({
             'name': request.locals['home'],
             'link': '/'
            })
    
    top_articles =  Article.objects.filter(is_published=True).order_by('-n_clicks').all()
    return render_to_response(request.site.settings.template + '/archive.html',
        {
            'issues': issues,
            'selected_menu': selected_menu,
            'site': request.site,
            'locals': request.locals,
            'main_menus': request.main_menus,
            'breadcrumb': breadcrumb,
            'top_articles': top_articles
        })
        
