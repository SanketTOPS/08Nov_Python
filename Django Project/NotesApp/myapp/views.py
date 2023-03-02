from django.shortcuts import render,redirect
from .forms import signupForm,notesForm
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

            uid=user_signup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=user_signup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm #create session
                request.session['userid']=uid.id
                return redirect('notes')
            else:
                print("Error! Login fail")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been uploaded!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def contact(request):
    return render(request,'contact.html')
    
def profile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=user_signup.objects.get(id=uid)
    return render(request,'profile.html',{'user':user,'cuser':user_signup.objects.get(id=uid)})

def userlogout(request):
    logout(request)
    return redirect('/')
