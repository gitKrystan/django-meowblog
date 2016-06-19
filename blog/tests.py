from django.test import TestCase

from .models import Post
from .factories import PostFactory


class PostMethodTests(TestCase):
    def test_was_created_with_proper_attributes(self):
        """
        Posts should be created when constructor is given the proper attributes
        """
        post = PostFactory()
        self.assertEqual(Post.objects.last(), post)
