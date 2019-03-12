from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['username'], password=request.POST['psw'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})

    return render(request, 'login.html')

def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect("home")


def signup(request):
    if request.method == 'POST':
        try:
            if request.POST['psw1'] == request.POST['psw2']:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html',{'error' : 'user has already been taken'})
            else:
                return render(request, 'signup.html', {'error': 'password must match'})

        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], password=request.POST['psw1'])
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'signup.html')