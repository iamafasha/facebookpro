from rest_framework import routers
from post import api_views as post_views

from user import api_views as user_views


router = routers.DefaultRouter()
router.register(r'posts', post_views.PostViewSet)
router.register(r'comments', post_views.CommentViewSet)
router.register(r'account/register', user_views.UserCreateSet)