from django.contrib import admin
from django.urls import path, include
from core.views import index, dashboard
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", dashboard, name="dashboard"),
    path("", index, name="index"),
    path('account/', include("accounts.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)