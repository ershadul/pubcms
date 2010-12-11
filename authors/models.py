from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(default=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    is_regular = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order', 'name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/author/%s' % (self.id)