from django.conf import settings
from django.core.urlresolvers import reverse
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

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def user_is_author(view):
        return view.get_object().author == view.request.user
