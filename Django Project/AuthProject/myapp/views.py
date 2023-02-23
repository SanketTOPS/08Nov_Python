from django.shortcuts import render,redirect
from .forms import signupForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect("/")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def userlogin(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Successfull!")
            request.session['user']=unm #create a session
            return redirect('home')
        else:
            print("Error! Login fail")
    return render(request,'userlogin.html')

def home(request):
    data=request.session.get('user')
    return render(request,'home.html',{'data':data})

def userlogout(request):
    logout(request)
    return redirect('/')
