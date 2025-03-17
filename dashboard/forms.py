from django import forms
from blogs.models import Category, Blogs, User
from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = (
            "title",
            "category",
            "blog_image",
            "short_description",
            "blog_body",
            "status",
            "is_feacherd"
        )


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )

