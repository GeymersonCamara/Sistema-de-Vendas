from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator  # Importando Paginator
from core.models import Evento

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

@login_required(login_url='/login/')
def cad_clientes(request):
    return render(request, 'clientes.html')

@login_required(login_url= '/login/')
def cad_produtos(request):
    return render(request, 'produtos.html')