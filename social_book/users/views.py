from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been created. You can log in now!')    
            return redirect('login.html')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)