from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('enrollment_number', 'first_name', 'is_staff', 'is_active',)
    list_filter = ('enrollment_number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('enrollment_number', ('first_name', 'last_name'), 'password', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('enrollment_number', 'password1', 'password2', ('first_name', 'last_name'), 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('enrollment_number',)
    ordering = ('enrollment_number',)

admin.site.register(User, CustomUserAdmin)