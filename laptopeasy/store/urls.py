from django.urls import path
from .views import LaptopListView, LaptopDetailView, LaptopCreateView, listing_success

urlpatterns = [
    path('', LaptopListView.as_view(), name='laptop_list'),
    path('laptop/<int:pk>/', LaptopDetailView.as_view(), name='laptop_detail'),
    path('list-your-laptop/', LaptopCreateView.as_view(), name='laptop_create'),
    path('success/', listing_success, name='listing_success'),
]