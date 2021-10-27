# app URLs

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoListView.as_view(), name='photo_list'),
    path('<int:pk>', views.PhotoDetailView.as_view(), name='photo_detail')
]