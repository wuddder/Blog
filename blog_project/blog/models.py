from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here
class Post(models.Model):
    author         = models.ForeignKey('auth.User')
    title          = models.CharField(max_length=200)
    text           = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    created_at     = models.DateTimeField(default=timezone.now())
    update_at      = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwarg={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post       = models.ForeignKey('blog.Post', related_name='comments')
    author     = models.CharField(max_length=200)
    text       = models.TextField()
    approved   = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
