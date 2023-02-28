from django.shortcuts import render,redirect
from .forms import signupForm
from .models import user_signup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get("login")=="login":
            unm=request.POST['username']
            pas=request.POST['password']

            user=user_signup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm #create session
                return redirect('notes')
            else:
                print("Error! Login fail")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def contact(request):
    return render(request,'contact.html')
    
def profile(request):
    return render(request,'profile.html')

def userlogout(request):
    logout(request)
    return redirect('/')
