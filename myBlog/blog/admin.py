from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    list_display = ['author','date']
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['id']
    inlines = [CommentInline]
admin.site.register(Post,PostAdmin)