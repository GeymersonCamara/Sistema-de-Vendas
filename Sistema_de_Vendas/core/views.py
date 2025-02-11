from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator  # Importando Paginator
from core.models import Evento
from core.models import Cliente
from core.forms import ClienteForm
from core.models import Product
from django import forms
from django.db import IntegrityError
from core.forms import ProductForm
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path

# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def pag_mercado(request):
    return render(request, 'mercado.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Certifique-se de usar request.POST corretamente
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)  # username é o padrão do Django
        if usuario is not None:
            login(request, usuario)
            return redirect('/principal/')  # Redireciona ao login com sucesso
        else:
            messages.error(request, "Usuario ou senha invalido!")  # Exibe erro
    return redirect('/login/')  # Garante um redirecionamento no caso de método não POST

def pag_inicio(request):
    return render(request, 'agenda.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'principal.html', dados)


@login_required(login_url= '/login/')
def cad_produtos(request):
    return render(request, 'produtos.html')

@login_required(login_url='/login/')
def cad_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Cliente cadastrado com sucesso!")
                return redirect('clientes')  # Redireciona para a lista de clientes
            except IntegrityError:
                messages.error(request, "Erro: CPF ou e-mail já cadastrado!")
        else:
            messages.error(request, "Erro ao cadastrar cliente. Verifique os dados.")

    else:
        form = ClienteForm()
    
    clientes = Cliente.objects.all()  # Buscar os clientes cadastrados
    return render(request, 'clientes.html', {'clientes': clientes, 'form': form})