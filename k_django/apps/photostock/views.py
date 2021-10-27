from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models import Photo
from django.views.generic import ListView, DetailView



class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo