from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trending', views.trending_songs, name='trending'),
]