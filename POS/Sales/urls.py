from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Sales-Home'),
    path('about/', views.about, name='Sales-about'),
]