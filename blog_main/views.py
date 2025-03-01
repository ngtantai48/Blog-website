from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import RegistrationForm


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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
