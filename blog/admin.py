from django.contrib import admin

# Register yousr models here.
from .models import Post
admin.site.register(Post)
