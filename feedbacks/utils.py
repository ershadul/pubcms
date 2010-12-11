from pubcms.feedbacks.models import Feedback

from django.conf import settings
from django.core.mail import send_mail

def send_feedbacks():
    feedbacks = Feedback.objects.all()
    for feedback in feedbacks:
        print feedback.id, feedback.get_sender()
        try:
            send_mail(feedback.name, feedback.message, feedback.email,
                      [settings.FEEDBACK_EMAIL])
        except Exception, e:
            print e