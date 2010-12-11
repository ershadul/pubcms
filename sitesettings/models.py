from django.db import models
from django.contrib.sites.models import Site

site_templates = (
    ('time', 'Time Magazine'),
)

default_template = 'msnbc'

class SiteSettings(models.Model):
    site = models.OneToOneField(Site, related_name="settings")
    slogan = models.CharField(max_length=256, default='A Django Site', blank=True)
    is_offline = models.BooleanField(default=False)
    offline_message = models.TextField(null=True, default='Please wait... We are improving our app.')
    copyright_text = models.CharField(max_length=256, null=True, blank=True)
    about_us = models.TextField(null=True, blank=True)
    contact_us = models.TextField(null=True, blank=True)
    robots_txt = models.TextField(null=True, blank=True, default='')
    template = models.CharField(max_length=15, choices=site_templates, default=default_template)

    class Meta:
        verbose_name = 'Site Configuration'
    
    def get_copyright_info(self):
        if self.copyright_text:
            return self.copyright_text
        else:
            return u'(C) %s' % (self.site.name)

    def __unicode__(self):
        return self.site.name

