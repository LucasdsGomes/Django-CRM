from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Costumer

def home(request):
    costumers = Costumer.objects.all()
    
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
        return render(request, 'home.html', {'costumers': costumers})

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi deslogado com sucesso.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        formulario = SignUpForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você foi registrado com sucesso.")
            return redirect('home')
        else:
            return render(request, 'register.html', {'formulario': formulario})
    else:
        formulario = SignUpForm()
        return render(request, 'register.html', {'formulario': formulario})
    
def costumer_record(request, pk):
    if request.user.is_authenticated: 
        thecostumer_record = Costumer.objects.get(id=pk)
        return render(request, 'record.html', {'thecostumer_record': thecostumer_record})
    else:
        messages.error(request, "Você deve estar logado para acessar esta página")
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated: 
        deletar = Costumer.objects.get(id=pk)
        deletar.delete()
        messages.success(request, "Você excluiu o usuário com sucesso.")
        return redirect('home')
    else:
        messages.error(request, "Você deve estar logado para deletar um usuário")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)      
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Usuário adicionado!")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "Você deve estar logado para efetuar tal ação")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        atual_record = Costumer.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=atual_record)   
        if form.is_valid():
            form.save()
            messages.success(request, "O usuário foi atualizado")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "Você deve estar logado para efetuar tal ação")
        return redirect('home')
    
