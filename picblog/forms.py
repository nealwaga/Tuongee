

from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ('title', 'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control','value':'','id':'naam'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }   

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','body')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
