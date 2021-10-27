from django.forms import fields
from .models import Photo
from django import forms


class PostForm(forms.ModelForm):

    class Meta():
        model = Photo
        fields = ('title', 'image', 'category', 'description')