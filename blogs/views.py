from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Category


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with id category_id
    posts = Blogs.objects.filter(status="published", category=category_id)

    # use try/except when we want to do some custom action if the category does not exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')

    # use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
        "posts": posts, 
        "category": category
    }
    return render(request, "posts_by_category.html", context)
