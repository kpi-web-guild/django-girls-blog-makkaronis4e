"""Description for models for interfacing the DB."""
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Blog post structure declaration."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        """Publish post in blog."""
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        """Publish post in blog."""
        return reverse('post_detail', kwargs={'pk': self.id})

    def __str__(self):
        """Render the post instance from its title."""
        return self.title

    @property
    def approved_comments(self):
        """Show comments that are ok in user's opinion."""
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """Model for comments."""

    post = models.ForeignKey('main.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def approve(self):
        """Approve comment and save it in DB."""
        self.is_approved = True
        self.save()

    def __str__(self):
        """Render Comment instance as its text by default when stringifying."""
        return self.text
