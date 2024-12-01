from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# common fields for all roles

class BaseUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# Form for Customers
class CustomerRegistrationForm(BaseUserRegistrationForm):
    def save(self, commit = True):
        user = super().save(commit=False)
        user.role = 'customer'
        if commit:
            user.save()
        return user
    
# Form for Staff
class StaffRegistrationForm(BaseUserRegistrationForm):
    def save(self, commit = True):
        user = super().save(commit=False)
        user.role = 'staff'
        if commit:
            user.save()
        return user