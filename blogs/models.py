import uuid
from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    objects = Manager
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(TimeStampedModel):
    category_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ("draft", "Draft"), 
    ("published", "Published")
)


class Blogs(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to="uploads/%y/%m/%d")
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField(max_length=3000)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="draft")
    is_feacherd = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    
    def __str__(self):
        return self.comment
    