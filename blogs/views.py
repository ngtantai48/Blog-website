from django.shortcuts import render, HttpResponse
from .models import Blogs


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with id category_id
    posts = Blogs.objects.filter(status="published", category=category_id)
    context = {
        "posts": posts
    }
    return render(request, "posts_by_category.html", context)
