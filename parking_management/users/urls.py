from django.urls import path
from . import views

urlpatterns = [
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/staff/', views.register_staff, name='register_staff'), 
]
