# -*- coding: utf-8 -*-

# section model
from django.db import models

class PublishedSectionManager(models.Manager):
    def get_query_set(self):
        return super(PublishedSectionManager, self).get_query_set().filter(is_published=True)

class UnpublishedSectionManager(models.Manager):
    def get_query_set(self):
        return super(PublishedSectionManager, self).get_query_set().filter(is_published=False)

class Section(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child_sections')
    title = models.CharField(max_length=256)
    tag_line = models.CharField(max_length=256, blank=True, default='')
    keywords = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    
    is_published = models.BooleanField(default=True)
    is_regular = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    
    objects = models.Manager()
    published_sections = PublishedSectionManager()
    unpublished_sections = UnpublishedSectionManager()

    class Meta:
        ordering = ['order']
    
    def __unicode__(self):
        if self.parent:
            return u'%s: %s' % (self.parent.title, self.title)
        return  self.title
    
    def get_absolute_url(self):
        return '/section/%s' % (self.id)