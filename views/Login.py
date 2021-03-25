from django.shortcuts import render, redirect, HttpResponse
from .form import Reg
from django.contrib import messages
from django.contrib .auth import authenticate, login, logout
from .models import registartion
from django.contrib.auth.hashers import make_password,check_password



def log(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        registartion = authenticate(request, username=username, password=password)

        if registartion is not None:
            login(request, registartion)
            return redirect('home')
        else:
            messages.info(request, 'username or password in wrong')
    context = {}
    return render(request, 'log.html',context)

def logoutuser(request):
    logout(request)
    return redirect('log')

