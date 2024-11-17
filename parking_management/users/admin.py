from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets +  (
        (None, {
            "fields": (
                'role', 'phone_number', 'address'
            ),
        }),
    )

    list_display = ['username', 'email', 'role', 'phone_number']
    
