from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('inner',views.inner_page,name='inner'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('login/',views.login,name='login'),
    path('login2/',views.login2,name='login2'),
    path('category/',views.category,name='category'),
    path('reg/',views.Registraion,name='reg'),
    path('about/',views.About,name='about'),
    path('services/',views.Services,name='services'),
]
