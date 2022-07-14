
from multiprocessing import context
from pydoc import render_doc
from django.shortcuts import redirect, render
from .models import Authentication, Categories, SellerProfile
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User


# Create your views here.
def Home(request):
    category=request.GET.get('category')
    
    if category == None:
        user_details = Authentication.objects.all()
    else:
        user_details = Authentication.objects.filter(category__category_name = category)
        
        
    catergories = Categories.objects.all()
    context = {'user':user_details,'catergories':catergories}
    return render(request,"base/index.html", context)

def Products_View(request,pk):
    products=Authentication.objects.all()
    product = Authentication.objects.get(id= pk)
    context = {'product':product,'products':products}
    
    return render(request,"base/product-spotlight.html", context)

def UserRegistraion(request):
    form = CustomUserRegistrationForm()
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
            
            
    
    context={'form':form}
    return render(request, "base/registration.html",context )

def LoginUser(request):
    
    user=User.objects.all()
    if request.method=="POST":
        username=request.POST['username'].lower()
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            return redirect("/")

    
        return redirect("home")

    if request.user.is_authenticated:
        return redirect("home")


    context={'profile':user}
    return render(request,'base/login.html', context)

def NavbarHandle(request):
    UserCredentials=SellerProfile.objects.all()
    context = {'userCred':UserCredentials}
    return render(request, 'base/navbar.html', context)
    