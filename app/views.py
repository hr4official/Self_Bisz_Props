from django.shortcuts import render, redirect, HttpResponse
from .form import Reg
from django.contrib import messages
from django.contrib .auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import registartion
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def inner_page(request):
    return render(request,'inner-page.html')

def business_profile(request):
    return render(request,'business profile.html')

def category(request):
    return render(request,'category.html')

def subcategories(request):
    return render(request,'subcategories.html')

def all_classifieds_cat(request):
    return render(request,'all-classifieds_cat.html')

# Subcategory

def Technology(request):
    return render(request,'Technology.html')

def Vehical(request):
    return render(request,'vehical.html')

def Electronics_applices(request):
    return render(request,'electronics-appliances.html')

def Fashion(request):
    return render(request,'fashion.html')

def Furnitures(request):
    return render(request,'furnitures.html')

def Kids(request):
    return render(request,'kids.html')

def Pets(request):
    return render(request,'pets.html')

def Real_estate(request):
    return render(request,'real-estate.html')

# Subcategory End

def About(request):
    return render(request,'about.html')

def Services(request):
    return render(request,'services.html')

# def final_reg(request):
#     return render(request,'final_reg.html')

# def final_login(request):
#     return render(request,'final_login.html')

def final_forgot(request):
    return render(request,'final_forgot.html')

# def login(request):
#     return render(request,'login.html')

# def reg(request):
#     return render(request,'reg.html')

def footar(request):
    return render(request,'footar.html')

def header(request):
    return render(request,'header.html')

def FAQ(request):
    return render(request,'FAQ.html')



# Create your views here.




@login_required(login_url='final_log')
def index(request):
    name = request.user.username
    return render(request, 'index.html', {'username': name})



def final_reg(request):
    
    # ency = make_password('12345')
    # print(ency)
    
    # decy = check_password('12345','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps=')
    # print(decy)
    
    print(make_password('12345'))
    print(check_password('123g45','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps='))
    form = Reg()
    if request.method == 'POST':
        form = Reg(request.POST)
        if form.is_valid():
            registartion.password = make_password('registartion.password')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "account was created for" + user)
        return redirect('final_log')
    context = {'form': form}
    return render(request, 'final_reg.html', context)


def final_log(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        registartion = authenticate(request, username=username, password=password)

        if registartion is not None:
            login(request, registartion)
            return redirect('index')
        else:
            messages.info(request, 'username or password in wrong')
    context = {}
    return render(request, 'final_log.html',context)


def logoutuser(request):
    logout(request)
    return redirect('final_log')


