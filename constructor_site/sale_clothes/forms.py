from django import forms
from .models import Demand, Comment


class DemandForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['title', 'phone']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']