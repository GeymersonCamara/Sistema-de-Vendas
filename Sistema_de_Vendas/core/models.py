from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M')
    
def validar_cpf(value):
    """Valida se o CPF está no formato correto (XXX.XXX.XXX-XX)."""
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError("CPF deve estar no formato XXX.XXX.XXX-XX")

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=14, 
        unique=True,
        validators=[validar_cpf]  # Adicionando a validação
    ) 
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
