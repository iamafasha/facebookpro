from django import template
from post.models import PostLike

register = template.Library()


@register.filter
def is_post_liked_by(things,user):
    try:
        PostLike.objects.get(post=things , author= user)
        return True
    except PostLike.DoesNotExist:
        return False
    return False