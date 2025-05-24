from django.contrib import admin
from .models import (
    Resume
)
# Basic model registrations

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('NAME', 'TITLE', 'status')
    search_fields = ('NAME', 'TITLE')
