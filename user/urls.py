from django.urls import path
from . import views

urlpatterns = [
    path('logout/',views.logout,name="logout"),
    path('profile/',views.settings, name="profile"),
    path('profile/settings',views.settings,name="settings"),
    path('register/',views.register,name="register"),
    path('', views.index, name="home"),
]