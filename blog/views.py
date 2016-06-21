from django.views import generic

from .models import Post


class PostList(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        """
        Return the most recently updated posts.
        """
        return Post.objects.order_by('-timestamp_last_modified')


class PostDetail(generic.DetailView):
    model = Post


class PostCreate(generic.edit.CreateView):
    model = Post
    fields = ['title', 'content', 'author']
