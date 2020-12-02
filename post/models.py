from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField( default=timezone.now, blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.text[0:100]

class PostLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

class PostMedia(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to = 'images/',blank=True, null=True)
    caption = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.post.text[0:40]

class Comment(models.Model):
    reply_to = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def comment(self):
        self.save()

    def filtered_unapproved_set(self):
        pass

    def __str__(self):
        return self.text[0:50]