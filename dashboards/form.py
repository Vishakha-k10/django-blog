from django import forms

from blogs.models import Category

class CategoryForm(forms.ModelForm):
    class meta:
        model=Category
        fields='__all__'