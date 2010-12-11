from django.contrib import admin
from pubcms.authors.models import Author

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'description', 'phone', 'address', 'designation']
    list_display = ['id', 'name', 'designation', 'email', 'phone', 'address', 'is_regular', 'order']
    list_editable = ('name', 'designation', 'is_regular', 'order',)

admin.site.register(Author, AuthorAdmin)
