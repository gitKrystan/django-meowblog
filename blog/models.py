from django.conf import settings
from django.db import models


class Post(models.Model):
    """
    Blog posts
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
