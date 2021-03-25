from django.shortcuts import render, redirect, HttpResponse
from .form import Reg
from django.contrib import messages
from django.contrib .auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import registartion
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.



@login_required(login_url='log')
def home(request):
    name = request.user.username
    return render(request, 'home.html', {'username': name})



def reg(request):
    
    print(make_password('12345'))
    print(check_password('123g45','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps='))
    form = Reg()
    if request.method == 'POST':
        form = Reg(request.POST)
        if form.is_valid():
            registartion.password = make_password('registartion.password')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "account was created for" + user)
        return redirect('log')
    context = {'form': form}
    return render(request, 'final_reg.html', context)





