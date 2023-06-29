"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage,name='signup'),
    path('login/', views.LoginPage,name = 'login'),
    path('home/', views.HomePage,name = 'home'),
    path('logout/', views.LogoutPage, name = 'logout'),
    path('home/booking/something', views.bookingPage, name = 'booking'),
    path('home/booking/test', views.selectDate, name = 'test'),
    # path('homeAdmin/', views.update_slots, name = 'homeAdmin'),
    path('homeAdmin/', views.AdminHomePage, name = 'homeAdmin'),
    path('loginAdmin/', views.LoginPageAdmin, name = 'loginAdmin'),
    path('homeAdmin/update_slots/<str:centre_name>/', views.update_slots, name='update_slots'),
    path('homeAdmin/delete_center/<str:centre_name>/', views.delete_center, name='delete_center'),
    path('homeAdmin/add_center/', views.add_center, name='add_center'),
    #  path('selectDate/<str:date>/', views.selectDate, name='select_date'),
    path('selectDate/', views.selectDate, name = 'selectDate'),
]


