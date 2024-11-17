from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser): 
    ROLE_CHOICE = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default='admin')
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Custom related name to avoid clashes
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Custom related name to avoid clashes
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
