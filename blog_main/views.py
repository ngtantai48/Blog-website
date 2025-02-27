from django.shortcuts import render
from blogs.models import Category, Blogs


def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_feacherd=True, status='published')
    posts = Blogs.objects.filter(is_feacherd=False, status='published')
    
    context = {
        "categories": categories,
        "featured_post": featured_post,
        "posts": posts
    }
    return render(request, "home.html", context)

