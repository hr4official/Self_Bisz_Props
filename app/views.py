from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def inner_page(request):
    return render(request,'inner-page.html')

def portfolio(request):
    return render(request,'portfolio-details.html')

def login(request):
    return render(request,'login.html')

def login2(request):
    return render(request,'login2.html')

def category(request):
    return render(request,'category.html')

def Registraion(request):
    return render(request,'reg.html')

def About(request):
    return render(request,'about.html')

def Services(request):
    return render(request,'services.html')