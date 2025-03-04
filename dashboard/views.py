from django.shortcuts import render
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()

    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts
    }

    return render(request, "dashboard/dashboard.html", context)
