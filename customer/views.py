
# from .forms import customer
# Create your views here.
from django.shortcuts import redirect, render
from .forms import CustomerSignupForm
from .models import Customer



def signup(request):
    customer= None
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            customer = Customer.objects.all()
            return render(request, 'customer/customer_details.html', {'customer':customer})
    else:
        form= CustomerSignupForm()
    return render(request, 'customer/signup.html', {'form':form,'customer':customer})
    

