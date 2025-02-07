from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #Maximo 100 caracteres para titulo
    descricao = models.TextField(blank=True, null=True) #Texto que pode deixar em branco ou null
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #Data do evento registrado
    data_criacao = models.DateTimeField(auto_now=True) #Data de quando o evento foi registrado
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M')