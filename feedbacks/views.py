from django.shortcuts import render_to_response
from pubcms.feedbacks.forms import FeedbackForm
from pubcms.feedbacks.models import Feedback
from pubcms.lib import captcha

def feedback(request):
    data = {}
    errors = {}
    
    message = ''
    successful = False
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = FeedbackForm(data)
        form.user = request.user
        if form.is_valid():
            feedback = Feedback()
            feedback.name = form.cleaned_data['name']
            feedback.email = form.cleaned_data['email']
            feedback.message = form.cleaned_data['message']
            if request.user.id:
                feedback.user = request.user
            feedback.save()
            successful = True
            message = request.locals['feedback_successful']
        else:
            errors = form.errors

    menus = request.main_menus
    selected_menu = None
    for m in menus:
        if m['name'] == 'feedback':
            m['is_selected'] = True
            selected_menu = m
            break
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

    (captcha_text, captcha_hash) = captcha.generate_captcha()
    
    return render_to_response(request.site.settings.template + '/feedback.html', {
        'selected_menu': selected_menu,
        'main_menus': menus,
        'breadcrumb': breadcrumb,
        'site': request.site,
        'locals': request.locals,
        'data': data,
        'errors': errors,
        'message': message,
        'successful': successful,
        'captcha_text': captcha_text,
        'captcha_hash': captcha_hash,
        'top_articles': request.top_articles
    })

