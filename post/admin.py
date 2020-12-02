from django.contrib import admin
from .models import Post, PostMedia,Comment,PostLike

admin.site.register(PostMedia)
admin.site.register(PostLike)
admin.site.register(Comment)

class PostMediaAdmin(admin.StackedInline):
    model = PostMedia
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostMediaAdmin]
 
    class Meta:
       model = Post

