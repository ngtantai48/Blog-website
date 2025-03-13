from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect


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
    # comments
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog = single_post)
    comment_count = comments.count()
    context = {
        'single_post': single_post,
        'comments': comments,
        'comment_count': comment_count
    }
    return render(request, "blogs.html", context)


# search functionality
def search(request):
    try:
        keyword = request.GET.get('keyword', '')
        if keyword:
            blogs = Blogs.objects.filter(
                Q(title__icontains=keyword) |
                Q(short_description__icontains=keyword) |
                Q(blog_body__icontains=keyword),
                status='published'
            )
        else:
            blogs = Blogs.objects.filter(status='published')

        context = {
            'blogs': blogs,
            'keyword': keyword
        }
        return render(request, 'search.html', context)
    
    except Exception as e:
        print(f"Error occurred in search function: {e}")
        return render(request, 'search.html', {'error': str(e)})
