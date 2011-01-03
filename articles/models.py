# -*- coding: utf-8 -*-

# article model
from django.db import models

from pubcms.authors.models import Author
from pubcms.sections.models import Section
from pubcms.issues.models import Issue

class DeferredBodyTextManager(models.Manager):
    def get_query_set(self):
        return super(DeferredBodyTextManager, self).get_query_set().defer('body_text')
    
class Article(models.Model):
    issue = models.ForeignKey(Issue, null=True, blank=True)
    section = models.ForeignKey(Section, null=True, blank=True)
    tag_line = models.CharField(max_length=256, blank=True, default='')
    title = models.CharField(max_length=256, default='', blank=True)
    slug_title = models.SlugField(max_length=256, blank=True, default='')
    part_number = models.CharField(max_length=10, default='', blank=True)
    intro_text = models.TextField(blank=True, default='')
    body_text = models.TextField()

    is_translated = models.BooleanField(default=False)
    author_name = models.CharField(max_length=255, null=True, blank=True)
    author_info = models.CharField(max_length=255, null=True, blank=True)
    translator_name = models.CharField(max_length=255, null=True, blank=True)
    translator_info = models.CharField(max_length=255, null=True, blank=True)

    keywords = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)

    authors = models.ManyToManyField(Author, blank=True, related_name='authored_articles')
    translators = models.ManyToManyField(Author, blank=True, related_name='translated_articles')
    
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    is_on_frontpage = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    n_clicks = models.IntegerField(default=0)
    n_retweets = models.IntegerField(default=0)
    n_buzz = models.IntegerField(default=0)
    n_fbshare = models.IntegerField(default=0)
    n_refers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    objects = DeferredBodyTextManager()
 
    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return "/issue/%s/article/%s" % (self.issue.published_at, self.id)
            
    def get_title(self):
        if not self.title:
            return self.section.title
        return self.title
    
    def __unicode__(self):
        if not self.title:
            return self.section.title
        return self.title

	

	
