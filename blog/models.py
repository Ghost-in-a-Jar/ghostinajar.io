from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)
    updated = models.DateTimeField(auto_now = True, auto_now_add=False)
    content_preview=' '.join(content.description.split(' ')[:50])



    def __unicode__(self):
        return unicode(self.title)