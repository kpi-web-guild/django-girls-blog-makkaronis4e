"""Views for blog app."""
from django.shortcuts import render  # noqa: F401


def post_list(request):
    """Render page with list of posts."""
    return render(request, 'blog/post_list.html', {})
