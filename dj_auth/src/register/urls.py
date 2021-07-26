from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser.as_view(), name="signup"),


]
