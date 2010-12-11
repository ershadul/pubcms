from django.contrib import admin
from pubcms.menus.models import MainMenu

class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'is_published', 'order')
    list_editable = ('order', 'is_published',)
admin.site.register(MainMenu, MainMenuAdmin)