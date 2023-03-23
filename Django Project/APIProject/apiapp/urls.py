from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('getalldata/',views.getalldata),
    path('getid/<int:id>/',views.getid),    
    path('saveuser/',views.saveuser),
    path('deleteuser/<int:id>/',views.deleteuser),
]
