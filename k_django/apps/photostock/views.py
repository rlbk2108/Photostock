from django.db import models
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models import Photo
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView



class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo
    context_object_name = 'photo'

class PhotoCreateView(CreateView):
    model = Photo
    context_object_name = 'photo'
    fields = '__all__'

class PhotoLoginView(LoginView):
    model = Photo
    template_name = 'registration/login.html'