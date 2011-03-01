from django.contrib import admin
from pubcms.articles.models import Article

def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = "Mark selected items as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_unpublished.short_description = "Mark selected items as unpublished"

def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)
make_featured.short_description = "Mark selected items as featured"

def make_not_featured(modeladmin, request, queryset):
    queryset.update(is_featured=False)
make_not_featured.short_description = "Mark selected items as not featured"

def publish_on_frontpage(modeladmin, request, queryset):
    queryset.update(is_on_frontpage=True)
publish_on_frontpage.short_description = "Publish selected items on frontpage"

def remove_from_frontpage(modeladmin, request, queryset):
    queryset.update(is_on_frontpage=False)
remove_from_frontpage.short_description = "Remove selected items from frontpage"

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro_text', 'body_text', 'tag_line', 'keywords', 'description']
    list_filter = ('is_featured', 'is_published', 'issue', 'section', 'is_translated', 'is_on_frontpage')
    list_display = ('id', 'issue', 'section', 'title', 'part_number', 'is_published',
        'is_translated', 'order', 'n_clicks', )
    list_editable = ('is_published', 'is_translated', 'order',)
    
    actions = [make_published, make_unpublished, make_featured, make_not_featured, publish_on_frontpage, remove_from_frontpage]

    fieldsets = (
        ('Issue And Section Information', {
            'fields': ('issue', 'section',)
        }),
        ('Article Title', {
            'fields': ('title', 'part_number', 'tag_line',)
        }),
        ('Article Content', {
            'fields': ('intro_text', 'body_text',)
        }),
        ('Author Information', {
            'fields': ('is_translated', 'author_name', 'author_info', 'translator_name', 'translator_info')
        }),
        ('Advanced Publishing Options', {
            'fields': ('is_published', 'order',) #'is_featured', 'is_on_frontpage')
        }),
        ('Search Engine Optimization', {
            'classes': ('collapse',),
            'fields': ('keywords', 'description',)
        }),

    )

    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )

admin.site.register(Article, ArticleAdmin)
