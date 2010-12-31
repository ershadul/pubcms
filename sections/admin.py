from django.contrib import admin
from pubcms.sections.models import Section

class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'title', 'is_published', 'is_regular', 'order']
    search_fields = ['title', 'tag_line', 'keywords', 'description']
    list_editable = ('is_published', 'is_regular', 'order', 'title',)
    ordering = ('parent', 'order',)
    list_filter = ('is_regular', 'is_published',)

    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )

admin.site.register(Section, SectionAdmin)
