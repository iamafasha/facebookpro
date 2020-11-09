from django.contrib import admin
from .models import Post, PostImage,Comment

admin.site.register(PostImage)
admin.site.register(Comment)

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Post

