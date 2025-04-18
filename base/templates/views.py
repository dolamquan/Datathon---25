from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q, Max, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def result(request):
    return render(request,'base/result.html')


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(request.POST)
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    
    return render(request,'base/register.html',{'form':form})
        


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    
    return render(request,'base/login.html')



def logoutUser(request):
    logout(request)
    return redirect('home')