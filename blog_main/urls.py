from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("blogs.urls")),
    path("register/", views.register, name="register"),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("dashboard/", include("dashboard.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
