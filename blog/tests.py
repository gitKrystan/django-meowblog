from django.core.urlresolvers import reverse
from django.test import TestCase

from .factories import PostFactory
from .models import Post


class PostMethodTests(TestCase):
    def test_was_created_with_proper_attributes(self):
        """
        Posts should be created when constructor is given the proper attributes
        """
        post = PostFactory()
        self.assertEqual(Post.objects.last(), post)


class PostViewTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no posts exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts.')

    def test_index_view_with_posts(self):
        """
        If posts exist, it displays them in reverse chronological order.
        """
        post1 = PostFactory(title="First Post")
        post2 = PostFactory(title="Second Post")
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertSequenceEqual(response.context['post_list'], [post2, post1])
