from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth,messages


def login(request):

    # if else yazmamizin sebebi ASP.NET uzerinde ayni metottan iki kez yazariz
    # ve bunun sebebi biri islem yapilacak ekran , digeri ise POST yapildiktan 
    # sonra yapilan islemlerdir.

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)

        if(user is not None):
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Oturum acildi')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Kullanici adi veya sifreniz yanlis')
            return redirect('login')
    else:
        return render(request,'user/login.html')

def logout(request):
    if(request.method == 'POST'):
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'Oturumunuz kapatildi')
        return redirect('index')
    else:
        return render(request,'user/logout.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if(password != repassword):
            messages.add_message(request, messages.WARNING, 'Parolalar eslesmiyor')
            return redirect('register')
        if(User.objects.filter(username = username).exists()):
            messages.add_message(request, messages.WARNING, 'Boyle bir kullanici var')
            return redirect('register')
        if(User.objects.filter(email = email).exists()):
            messages.add_message(request, messages.WARNING, 'Bu email daha once alinmis')
            return redirect('register')

        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Basariyla kayit oldunuz')
        return redirect('login')
        
    else:
        return render(request,'user/register.html')
