"""Views for blog app."""
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import (
    DetailView, ListView,
    UpdateView, View, CreateView,
)

from .forms import PostForm
from .models import Post


class Protected(View):
    """Protect views that need to show only for authorised users."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Rewrite standart method and it to decorator."""
        return super().dispatch(*args, **kwargs)


class PostList(ListView):
    """Show all your Post objects."""

    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        """Return needed posts."""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetail(DetailView):
    """Show info about one chosen post."""

    model = Post
    template_name = 'blog/post_detail.html'


class NewPost(CreateView, Protected):
    """Return page to add a new Post."""

    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        """Return post_detail after save changes in post."""
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        """Add info to form that were not given from POST request."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView, Protected):
    """Post edit view."""

    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        """Return post_detail after save changes in post."""
        return reverse('post_detail', kwargs={'pk': self.get_object().id})
