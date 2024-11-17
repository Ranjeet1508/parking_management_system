from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomerRegistrationForm, StaffRegistrationForm

# Create your views here.

# @login_required
# @user_passes_test(lambda u: u.role == 'customer', login_url='/login/')

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerRegistrationForm()        
    return render(request, 'customer/register_customer.html', {'form': form})
    

@login_required
@user_passes_test(lambda u: u.role == 'admin', login_url='/access-denied/')
def register_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = StaffRegistrationForm()    
    return render(request, 'staff/register_staff.html', {'form': form})
