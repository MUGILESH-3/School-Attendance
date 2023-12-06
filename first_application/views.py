from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse 
from .models import userregister
from .models import attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,"index.html")

def admin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=='admin' and password=='admin':
            return redirect('adminhome')
        else:
            return HttpResponse("Username or Password is incorrect") 
    
    return render(request,"admin.html")

def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        userobj = userregister.objects.filter(Username=username,Password=password)
        if userobj:
            return redirect('studentattendance')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request,"user.html")

def userreg(request):
    if request.method=='POST':
        name=request.POST['name']
        rollno=request.POST['rollno']
        username=request.POST['username']
        password=request.POST['password']

        obj=userregister()
        obj.Name=name
        obj.Rollno=rollno
        obj.Username=username
        obj.Password=password
        obj.save()

    return render(request,"userreg.html")

def userdetails(request):
    
    mydata=userregister.objects.all()
    return render(request,"userdetails.html",{'datas':mydata})
    #return render(request,"userdetails.html")

def studentattendance(request):
    if request.method=='POST':
        name=request.POST['name']
        rollno=request.POST['rollno']
        date=request.POST['date']
        

        obj=attendance()
        obj.Name=name
        obj.Rollno=rollno
        obj.Date=date
        obj.save()

    return render(request,"studentattendance.html")

def adminhome(request):
    atteddata=attendance.objects.all()
    return render(request,"adminhome.html",{'attend':atteddata})
    #return render(request,"adminhome.html")


