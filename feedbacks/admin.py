from django.contrib import admin
from pubcms.feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	search_fields = ['name', 'email', 'message']
	list_display = ('id', 'name', 'email', 'message', 'created_at',)

        class Media:
                js = ('/media/js/jquery-1.4.2.min.js',
                    '/media/js/tiny_mce/tiny_mce.js',
                    '/media/js/textareas.js',
                )

admin.site.register(Feedback, FeedbackAdmin)
