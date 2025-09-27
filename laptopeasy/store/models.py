from django.db import models
from django.urls import reverse

class Laptop(models.Model):
    name = models.CharField(max_length=200, help_text="e.g., MacBook Pro 13-inch 2020")
    description = models.TextField(help_text="Include specs like RAM, CPU, Storage, Condition, etc.")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='laptops/')

    # Seller Contact Info
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField()

    # Admin Approval
    is_approved = models.BooleanField(default=False, help_text="Approved by admin to be shown on the site")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.seller_name}"

    def get_absolute_url(self):
        return reverse('laptop_detail', args=[str(self.id)])