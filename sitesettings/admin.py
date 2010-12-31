from django.contrib import admin
from pubcms.sitesettings.models import SiteSettings

class SiteSettingsAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
            '/media/js/tiny_mce/tiny_mce.js',
            '/media/js/textareas.js',
        )

admin.site.register(SiteSettings, SiteSettingsAdmin)
