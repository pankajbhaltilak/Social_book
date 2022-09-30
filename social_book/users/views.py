from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegistrationForm
from django.db.models import Q


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
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def dashboard(request):
    if 'data' in request.GET:
        data = request.GET['data']
        user = User.objects.filter(roles__icontains=data)
        # multiple_data = Q(Q(public_visibility__icontains=data))

    else:
        user = User.objects.all()
    context = {
        'User': user
    }
    print(context)
    return render(request, 'dashboard.html', context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def search(request):
    queryset = User.objects.all()
    public_visibility = request.GET.get('public_visibility')

    if public_visibility == 'on':
        queryset = queryset.filter(public_visibility=True)

    # else:
    #     public_visibility = User.objects.all()
        
    context = {'queryset': queryset}
    print(context)
    return render(request, 'search.html', context)
