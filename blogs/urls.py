from django.urls import path
from . import views

urlpatterns = [
    path("blogs/search/", views.search, name="search"),
    path("blogs/<slug:slug>/", views.blogs, name="blogs"),
    path("category/<uuid:category_id>/", views.posts_by_category, name="posts_by_category")
]
