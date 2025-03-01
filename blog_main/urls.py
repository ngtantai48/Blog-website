from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as BlogsView

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("category/", include("blogs.urls")),
    path('<slug:slug>/', BlogsView.blogs, name='blogs')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
