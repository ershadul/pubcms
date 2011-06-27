# -*- coding: utf-8 -*-

# issue model
from django.db import models
from pubcms.sections.models import Section

class Issue(models.Model):
    title = models.CharField(max_length=256)
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    published_at = models.DateField(unique=True, db_index=True)
    issue_year = models.CharField(max_length=25, blank=True, default='')
    issue_number = models.CharField(max_length=25, blank=True, default='')
    is_default = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='covers', max_length=100, blank=True, null=True)
    keywords = models.TextField(blank=True, default='')
    description = models.TextField(default='', blank=True)
    sections = models.ManyToManyField(Section, null=True, blank=True, through='IssueSectionAssociation')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        
    def save(self, force_insert=False, force_update=False):
        if self.is_default:
            from django.db import connection, transaction
            cursor = connection.cursor()
            # Data modifying operation - commit required
            cursor.execute("UPDATE issues_issue SET is_default = 0 WHERE is_default = 1")
        super(Issue, self).save(force_insert=force_insert, force_update=force_update)

    def get_absolute_url(self):
        return '/issue/%s' % (self.published_at)
    
    def __unicode__(self):
            return self.title

class IssueSectionAssociation(models.Model):
    issue = models.ForeignKey(Issue)
    section = models.ForeignKey(Section)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']