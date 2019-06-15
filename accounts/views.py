from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def singup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user =User.objects.get (username = request.POST['username'])
                return render (request,"accounts/singup.html",{'error':'user name already taken'})
            except:
                user =User.objects.create_user (username = request.POST['username'] , password =request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/singup.html',{'error':"please confirm your password  are don't matched"})

    else:
        return render (request,"accounts/singup.html")




def login(request):
    if request.method=='POST':
        user =auth.authenticate (username = request.POST['username'] , password =request.POST['password'])
        auth.login(request,user)
        return redirect('home')
    else :
        return render (request,"accounts/login.html",{'error':'sorry  username or password incorrect!'})

    return render (request,"accounts/login.html")

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    