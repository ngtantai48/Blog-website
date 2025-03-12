from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Category, Comment
from django.db.models import Q


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with id category_id
    posts = Blogs.objects.filter(status="published", category=category_id)

    # use try/except when we want to do some custom action if the category does not exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect("home")

    # use get_object_or_404 when you want to show 404 error page if the category does not exist
    # category = get_object_or_404(Category, pk=category_id)

    context = {
        "posts": posts, 
        "category": category
    }
    return render(request, "posts_by_category.html", context)


# blogs
def blogs(request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    #comments
    comments = Comment.objects.filter(blog = single_post)
    comment_count = comments.count()
    context = {
        'single_post': single_post,
        'comments': comments,
        'comment_count': comment_count
    }
    return render(request, "blogs.html", context)


# search dunctionality
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) 
                                | Q(short_description__icontains=keyword) 
                                | Q(blog_body__icontains=keyword),
                                status='published'
    )
    content={
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', content)