from django.contrib import admin
from pubcms.feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	search_fields = ['name', 'email', 'message']
	list_display = ('id', 'name', 'email', 'message', 'created_at',)

admin.site.register(Feedback, FeedbackAdmin)
