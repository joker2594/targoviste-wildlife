from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime


class Post(models.Model):
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to='post_images')
    description = models.TextField(blank=True)
    date_added = models.DateTimeField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date_added)
        self.date_added = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug


