from django.contrib import admin
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register,name = "register"),
    path('login/', views.loginUser,name = "login"),
    path('logout/', views.logoutUser,name = "logout"),
    path('forgot/', views.forgot, name="forgot"),
    path('reset/', views.reset, name="reset"),
]