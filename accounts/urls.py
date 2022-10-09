from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('register/', register,name = "register"),
    path('login/', loginUser,name = "login"),
    path('logout/', logoutUser,name = "logout"),
    path('forgot/', forgot, name="forgot"),
    path('reset/', reset, name="reset"),
    path('profile/', profile, name="profile"),
    path("kullanici-girisi", registration_view, name = "authentication"),
    path("kullanici-cikisi", logout_view, name = "logout_account"),
    path('sifre-degistir/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]