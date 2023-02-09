from django.shortcuts import render,redirect
from .forms import userForm
from .models import userinfo

# Create your views here.

def index(request):
    if request.method=='POST':
        user=userForm(request.POST)
        if user.is_valid():
            user.save()
            print("Your data has been saved!")
        else:
            print(user.errors)
    return render(request,'index.html')


def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    cid=userinfo.objects.get(id=id)
    userinfo.delete(cid)
    return redirect('showdata')
