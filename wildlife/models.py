from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/default_user_picture.jpg')
    status = models.TextField(blank=True)
    ''' solve the issue of users with same profile usernames '''
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.username)
            super(UserProfile, self).save(*args, **kwargs)
            resized = get_thumbnail(self.picture, "200x200", crop="center")
            self.picture.save(resized.name, ContentFile(resized.read()), True)

        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True)
    picture = models.ImageField(upload_to='post_images', null=True)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.date_added = datetime.now()
        self.slug = slugify(self.date_added)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug


class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True)
    post = models.ForeignKey(Post, null=True)
    comment = models.TextField()
    date_added = models.DateTimeField()