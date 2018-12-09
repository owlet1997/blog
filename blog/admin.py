from django.contrib import admin
from .models import Post
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'user')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
