from django.contrib import admin
from pubcms.issues.models import Issue

class IssueAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'issue_year', 'issue_number']
    list_filter = ('is_published', 'is_default',)
    
    list_display = ('id', 'title', 'published_at', 'issue_year', 'issue_number', 'is_published', 'is_default',)
    list_editable = ('title', 'published_at', 'issue_year', 'issue_number', 'is_published', )
    exclude = ['sections']

    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )

admin.site.register(Issue, IssueAdmin)
