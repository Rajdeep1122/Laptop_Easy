from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Laptop
from .forms import LaptopForm

class LaptopListView(ListView):
    model = Laptop
    template_name = 'store/laptop_list.html'
    context_object_name = 'laptops'
    # Crucial: Only show listings that have been approved by an admin
    queryset = Laptop.objects.filter(is_approved=True).order_by('-created_at')

class LaptopDetailView(DetailView):
    model = Laptop
    template_name = 'store/laptop_detail.html'
    context_object_name = 'laptop'

class LaptopCreateView(CreateView):
    model = Laptop
    form_class = LaptopForm
    template_name = 'store/laptop_form.html'
    # Redirect to this page on successful form submission
    success_url = reverse_lazy('listing_success')

def listing_success(request):
    return render(request, 'store/listing_success.html')
