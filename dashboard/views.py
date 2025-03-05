from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method=="POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category modified successfully!")
            return redirect('categories')
        else:
            messages.error(request, "Failed to edit category. Please check the form.")
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, "dashboard/edit_categories.html", context)


def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
    # return render(request, 'dashboard/categories.html')