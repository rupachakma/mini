from django.shortcuts import redirect, render
from  Blog.forms import SignupForm,LoginForm 
from Blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    posts=Post.objects.all()

    return render(request,"home.html",{'posts':posts})

def signuppage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations !!")
            form.save()
        else:
            messages.error(request,"InValid your request")
    else:
        form = SignupForm()
        return render(request,'signup.html',{'form':form})
    return render(request,"signup.html",{'form':form})

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST )
            if form.is_valid():
                username = form.changed_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=username,password=userpass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Successfully logged in !!")
                    form.save()
                else:
                    messages.error(request,"InValid your request")
        else:
            form = LoginForm()
            return render(request,"login.html",{'form':form})
    else:
        return redirect('dashboardpage')

    return render(request,"login.html")

def dashboardpage(request):
    return render(request,"dashboard.html")

def contactpage(request):
    return render(request,"contact.html")

def aboutpage(request):
    return render(request,"about.html")

def logout(request):
    return redirect("loginpage")