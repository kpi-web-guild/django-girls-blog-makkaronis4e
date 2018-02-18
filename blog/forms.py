"""Forms setup."""
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for submitting the blog post."""

    class Meta:
        """Config for the post form."""

        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    """Comment model form."""

    class Meta:
        """Config for the comment form."""

        model = Comment
        fields = ('author', 'text')
