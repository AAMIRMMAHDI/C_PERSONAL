from django.contrib import admin
from .models import (
    Contact
)
# Basic model registrations



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('name', 'email', 'subject')
    actions = ['approve_contacts']

    def save_model(self, request, obj, form, change):
        if obj.response:  
            obj.is_approved = True  
        super().save_model(request, obj, form, change)

    def approve_contacts(self, request, queryset):
        queryset.update(is_approved=True)
    approve_contacts.short_description = "Approve selected contacts"

