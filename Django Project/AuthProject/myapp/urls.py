from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.userlogin),
    path('index/',views.index),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),
]