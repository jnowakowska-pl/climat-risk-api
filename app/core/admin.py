"""Django admin configuration for the core app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['user_id']
    list_display = ['email', 'username', 'created_at']
    list_filter = ['is_superuser', 'is_active']

admin.site.register(models.Users, UserAdmin)