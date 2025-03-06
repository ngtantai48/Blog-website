from django import forms
from blogs.models import Category, Blogs


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = (
            'title',
            'category',
            'blog_image',
            'short_description',
            'blog_body',
            'status',
            'is_feacherd'
        )
