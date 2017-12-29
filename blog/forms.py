"""Post form."""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Name of post form."""

    class Meta:
        """Show model which would be used for form."""

        model = Post
        fields = ('title', 'text',)
