from django.shortcuts import render, HttpResponse
from django.views import generic

from .models import Post


# def list(request):
#     latest_post_list = Post.objects.order_by('-timestamp_last_modified')[:5]
#     context = {
#         'latest_post_list': latest_post_list
#     }
#     return render(request, 'posts/list.html', context)

class ListView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        """
        Return the most recently updated posts.
        """
        return Post.objects.order_by('-timestamp_last_modified')
