from django.contrib import admin
from .models import (
    Stats, Skill, About,
)
# Basic model registrations




@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('happy_clients', 'projects', 'hours_of_support' ,'hard_workers')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage')
    ordering = ('-percentage',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('PAGE_NAME', 'CREATOR_NAME', 'status')
    list_filter = ('status',)
