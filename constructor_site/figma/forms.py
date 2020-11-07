from django import forms
from .models import Category
from .models import Good


class CategoryForm(forms.ModelForm):
        class Meta:
            model = Category 
            fields = ['title']


class GoodForm(forms.ModelForm):
        class Meta:
            model = Good 
            fields = ['title','price','top','category','photo',]