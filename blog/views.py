"""Views for blog app."""
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, View, DeleteView, TemplateView, CreateView

from .forms import CommentForm, PostForm
from .models import Post, Comment


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

    def form_valid(self, form):
        """Add info to form that were not given from POST request."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView, Protected):
    """Post edit view."""

    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'


class PostDraftList(ListView, Protected):
    """Return draft list."""

    queryset = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    context_object_name = 'posts'
    template_name = 'blog/post_draft_list.html'


class PublishPost(Protected, TemplateView):
    """View for publishing post."""

    def get(self, request, *args, **kwargs):
        """Get info about POst pk that we use."""
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post.publish()
        return redirect('post_detail', pk=post.pk)


class RemovePost(Protected, DeleteView):
    """View for deleting posts."""

    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_edit.html'


class AddCommentToPost(CreateView):
    """If someone wants to create new comment he/she get this view."""

    form_class = CommentForm
    template_name = 'blog/post_edit.html'

    def post(self, request, *args, **kwargs):
        """Add comment to DB."""
        post = get_object_or_404(Post, pk=kwargs['pk'])
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)


class ApproveComment(Protected, TemplateView):
    """Moderate comment."""

    def get(self, request, *args, **kwargs):
        """Approve comment and update info in DB."""
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        comment.approve()
        return redirect('post_detail', pk=comment.post.pk)


class RemoveComment(Protected, DeleteView):
    """Remove comment."""

    model = Comment
    template_name = 'blog/post_edit.html'

    def post(self, request, *args, **kwargs):
        """Rewritten standart method."""
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
