from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
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


class PostCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class UserOwnerMixin(UserPassesTestMixin):

    def test_func(self):
        """
        only allow post author to edit post
        """
        return self.get_object().author == self.request.user


class PostUpdate(UserOwnerMixin, generic.edit.UpdateView):
    model = Post
    fields = ['title', 'content']


class PostDelete(UserOwnerMixin, generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
