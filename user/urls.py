from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile/',views.settings, name="profile"),
    path('profile/settings',views.settings,name="settings"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),
]