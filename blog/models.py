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
