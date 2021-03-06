from django.urls import path
from .auth_views import RegisterView, LoginView
from .post_views import PostDetailView, PostListView, CommentListView , CommentDetailView , PostLikeViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Facebook Pro API",
        default_version='v1',
        description="An api this facebook project",
        terms_of_service="#",
        contact=openapi.Contact(email="me@iamafasha.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path("", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('sandbox/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/register/', RegisterView.as_view(), name ="api_register"),
    path('auth/login/', LoginView.as_view(), name="api_login" ),
    path('posts/', PostListView.as_view(),name="api_post_list"),
    path('posts/<int:id>/', PostDetailView.as_view(),name="api_post_single"),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(),name="api_comments_list"),
    path('posts/<int:post_id>/comments/<int:id>/', CommentDetailView.as_view(),name="api_coments_single"),
    path('posts/<int:post_id>/like/', PostLikeViewSet.as_view({'post': 'create','delete':'destroy'}) ,name="api_like"),
]