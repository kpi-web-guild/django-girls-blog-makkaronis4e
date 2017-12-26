"""Models configuration in blog."""
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Configuration of the post class."""

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

    def __str__(self):
        """Return title of the post."""
        return self.title
