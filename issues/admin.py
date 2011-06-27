from django.contrib import admin
from pubcms.issues.models import Issue, IssueSectionAssociation

class IssueSectionAssociationInline(admin.TabularInline):
    model = IssueSectionAssociation
    extra = 10

class IssueAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'issue_year', 'issue_number']
    list_filter = ('is_published', 'is_default',)
    
    list_display = ('id', 'title', 'published_at', 'issue_year', 'issue_number', 'is_published', 'is_default',)
    list_editable = ('title', 'published_at', 'issue_year', 'issue_number', 'is_published', )
    #exclude = ['sections']
    inlines = [IssueSectionAssociationInline,]

    class Media:
        js = (
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )

admin.site.register(Issue, IssueAdmin)
admin.site.register(IssueSectionAssociation)


