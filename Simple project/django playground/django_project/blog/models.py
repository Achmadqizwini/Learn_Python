from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"
        ordering = ['-published_at']

    def __str__(self):
        return self.title
