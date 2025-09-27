from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'description', 'price', 'image', 'seller_name', 'seller_email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control'}),
            'seller_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }