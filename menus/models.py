from django.db import models

class MainMenu(models.Model):
    title = models.CharField(max_length=128, unique=True)
    url = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.title
