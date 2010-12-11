from django import forms

from pubcms.feedbacks.models import Feedback
from pubcms.lib import captcha

class FeedbackForm(forms.Form):
    captcha_hash = forms.CharField(required=True)
    name = forms.CharField(required=True, max_length=50,
        error_messages={
            'required': 'Please enter your name'
        }
    )
    email = forms.EmailField(required=True,
         error_messages={
            'required': 'Please enter your email'
        }
    )
    message = forms.CharField(required=True,
        error_messages={'required': 'Please enter your feedback'})

    captcha_text = forms.CharField(required=True,
        error_messages={'required': 'Please answer the math question'})

    def clean_captcha_text(self):
        if  captcha.check_captcha(self.cleaned_data['captcha_text'],
                self.cleaned_data['captcha_hash']):
            return self.cleaned_data['captcha_text']
        else:
            raise  forms.ValidationError('Please anser the math question correctly')
        

