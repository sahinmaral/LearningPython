from django.shortcuts import render

def login(request):
    return render(request,'user/login.html')

def logout(request):
    return render(request,'user/logout.html')

def register(request):
    return render(request,'user/register.html')
