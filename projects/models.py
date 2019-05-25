from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile


# Create your models here.

class Post(models.Model):
    post_image = models.ImageField(upload_to='projects_pics/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Rating(models.Model):
    design = models.IntegerField(blank=True, default=0)
    usability = models.IntegerField(blank=True, default=0)
    content = models.IntegerField(blank=True, default=0)
    average_score = models.IntegerField(blank=True, default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
