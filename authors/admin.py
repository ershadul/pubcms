from django.contrib import admin
from pubcms.authors.models import Author

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'description', 'phone', 'address', 'designation']
    list_display = ['id', 'name', 'designation', 'email', 'phone', 'address', 'is_regular', 'order']
    list_editable = ('name', 'designation', 'is_regular', 'order',)

    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )

admin.site.register(Author, AuthorAdmin)
