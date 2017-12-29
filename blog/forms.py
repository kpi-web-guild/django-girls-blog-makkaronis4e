"""Forms setup."""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for submitting the blog post."""

    class Meta:
        """Config for the post form."""

        model = Post
        fields = ('title', 'text',)
