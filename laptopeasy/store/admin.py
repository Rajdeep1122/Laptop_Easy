from django.contrib import admin
from .models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller_name', 'price', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    list_editable = ('is_approved',) # Allows direct editing in the list view
    search_fields = ('name', 'description', 'seller_name', 'seller_email')
    actions = ['approve_listings']

    def approve_listings(self, request, queryset):
        queryset.update(is_approved=True)
    approve_listings.short_description = "Approve selected listings"
