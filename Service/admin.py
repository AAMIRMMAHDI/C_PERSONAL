from django.contrib import admin
from .models import (
    Service, ServiceComment
)

# Basic model registrations
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'content')
