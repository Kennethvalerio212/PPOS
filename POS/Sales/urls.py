from django.urls import path
from .views import (
    SalesCreateView,SalesListView,SalesDeleteView,SalesUpdateView,SalesDetailView
)
from . import views




urlpatterns = [
    path('', SalesListView.as_view(), name='Sales-home'),
    path('product/new/', SalesCreateView.as_view(), name='add-prod'),
    path('product/<int:pk>/', SalesDetailView.as_view(), name='prod-details'),
    path('product/<int:pk>/update/', SalesUpdateView.as_view(), name='prod-update'),
    path('product/<int:pk>/delete/', SalesDeleteView.as_view(), name='prod-delete'),
    path('about/', views.about, name='Sales-about'),
]