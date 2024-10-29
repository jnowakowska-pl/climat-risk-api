"""Django admin configuration for the core app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    order = ['id']
    list_display = ['email', 'username']

admin.site.register(models.User, UserAdmin)