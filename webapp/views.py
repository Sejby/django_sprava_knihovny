from django.shortcuts import render, redirect
from .forms import RegistracniFormular,LoginFormular

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate 
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Kniha

def uvod(request):
    return render(request, 'webapp/index.html')

def registrace(request):
    formular = RegistracniFormular()
    if request.method == "POST" :
        formular = RegistracniFormular(request.POST)
        if formular.is_valid():
            formular.save()
            messages.success(request, "Úspěšně vytvořen profil!")
            return redirect('prihlaseni')
        else:
            messages.warning(request, 'Formulář byl špatně vyplněn!')
        
    context={'form': formular}
    return render(request, 'webapp/register.html', context=context)

def prihlaseni(request):
    formular = LoginFormular()
    if request.method == "POST":
        formular = LoginFormular(request, data=request.POST)
        if formular.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    return render(request, 'webapp/login.html', context={'form': formular})

def odhlaseni(request):
    auth.logout(request)
    return redirect('uvod')

@login_required(login_url='prihlaseni')
def dashboard(request):
    return render(request, 'webapp/dashboard.html')