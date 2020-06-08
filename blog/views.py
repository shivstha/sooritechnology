from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog_detail.html'


def post_detail(request, slug_name):
    post = get_object_or_404(Post, slug=slug_name,
                             status='published', )
    return render(request,
                  'blog_detail.html',
                  {'post': post,
                   })
