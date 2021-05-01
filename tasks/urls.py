from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name="login"),
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('create', views.create, name="create"),
    path('navbar', views.navbar, name="navbar"),
    path('logout', views.user_logout, name="logout"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('read/<int:id>', views.read, name="read"),
]
