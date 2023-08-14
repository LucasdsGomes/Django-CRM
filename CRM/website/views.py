from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            messages.success(request, "Você efetuou login com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Ocorreu um erro ao efetuar login. Por favor, tente novamente.")
            return redirect('home')
    else:
        return render(request, 'home.html',  {})

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi deslogado com sucesso.")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})