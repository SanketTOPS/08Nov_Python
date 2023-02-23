from django.contrib import admin
from django.urls import path,include
from covidapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('doctors/',views.doctors),
    path('news/',views.news),
    path('protect/',views.protect),
]
