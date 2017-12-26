"""Admin panel registration."""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
