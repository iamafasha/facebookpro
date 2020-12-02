from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/', views.profile , name="profile" ),
    path('add_post/',views.create_post,name="create_post"),
    path('<int:post_id>/comments/create',views.create_comment,name="add_comment"),
    path('<int:post_id>/comment/<int:comment_id>/',views.comment,name="comment"),
    path('<int:id>/', views.single_post , name="sinlge_post" ),
]
