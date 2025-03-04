from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blogs.models import Category, Blogs
from dashboard.forms import CategoryForm


@login_required(login_url="login")
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()

    context = {
        "category_counts": category_counts, 
        "blogs_counts": blogs_counts
    }

    return render(request, "dashboard/dashboard.html", context)


def categories(request):
    return render(request, "dashboard/categories.html")


def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            return redirect("categories")
        else:
            messages.error(request, "Failed to create category. Please check the form.")
    form = CategoryForm()

    context = {
        "form": form
    }
    return render(request, "dashboard/add_categories.html", context)
