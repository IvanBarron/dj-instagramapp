from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'picture', 'created_at', 'modified_at')

