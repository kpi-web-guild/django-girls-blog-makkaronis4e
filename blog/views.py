"""Views for blog app."""
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, UpdateView, View, FormView

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
    """Show info about one post you have chosen."""

    model = Post
    template_name = 'blog/post_detail.html'


class NewPost(FormView, Protected):
    """Return page for adding new Post."""

    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        """Add info to form that were not given from POST request."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """Get info from form and save it as 'post' object."""
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)


class EditPost(UpdateView, Protected):
    """View is for editing post."""

    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_edit.html'
