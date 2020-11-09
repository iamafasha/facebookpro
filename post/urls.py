from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile , name="profile" ),
    path('<int:id>/', views.single_post , name="sinlge_post" ),
]
