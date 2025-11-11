from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        messages.success(request,"Registered Succesfully")
        return redirect('login')
    return render(request,'register.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"invalid credential")
    return render(request,'login.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
        