from django.contrib import admin
from django.urls import path, include
from core.views import index, dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", dashboard, name="dashboard"),
    path("", index, name="index"),
    path('account/', include("accounts.urls")),
]
