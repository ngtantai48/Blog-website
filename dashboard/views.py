from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib import messages
from blogs.models import Category, Blogs, User
from dashboard.forms import CategoryForm, BlogForm, AddUserForm, EditUserForm


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
            print('Errors: ', form.errors)
            messages.error(request, "Failed to create category. Please check the form.")

    form = CategoryForm()
    context = {
        "form": form
    }
    return render(request, "dashboard/add_categories.html", context)


def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category modified successfully!")
            return redirect("categories")
        else:
            print('Errors: ', form.errors)
            messages.error(request, "Failed to edit category. Please check the form.")

    form = CategoryForm(instance=category)
    context = {
        "form": form, 
        "category": category
    }
    return render(request, "dashboard/edit_categories.html", context)


def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")
    # return render(request, 'dashboard/categories.html')


def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "dashboard/posts.html", context)


def add_posts(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(form.cleaned_data['title'])
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("posts")
        else:
            error_messages = "\n".join([f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()])
            print('Errors: ', error_messages)
            messages.error(request, "Failed to create post. Please check the form.")

    form = BlogForm()
    context = {
        "form": form
    }
    return render(request, "dashboard/add_posts.html", context)


def edit_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(form.cleaned_data["title"])
            post.save()
            messages.success(request, "Post updated successfully!")
            return redirect("posts")
        else:
            messages.error(request, "Failed to update post. Please check the form.")

    form = BlogForm(instance=post)
    context = {
        "form": form,
        "post": post
    }
    return render(request, "dashboard/edit_posts.html", context)


def delete_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect("posts")


def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/users.html', context)


def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_users.html', context)


def edit_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit user info successfully!")
            return redirect('users')
        else:
            messages.error(request, "Failed to edit user. Please check the form.")
    
    form = EditUserForm(instance=user)
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'dashboard/edit_users.html', context)


def delete_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("users")

