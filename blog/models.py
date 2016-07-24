from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)
    updated = models.DateTimeField(auto_now = True, auto_now_add=False)

    slug = models.SlugField(unique=True)

    @permalink
    def get_absolute_url(self):
        return ('post', (),
                {
                    'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.content