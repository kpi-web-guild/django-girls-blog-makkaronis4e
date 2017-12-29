"""Views for blog app."""
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404


def post_list(request):
    """Render page with list of posts."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Render detailed post."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
