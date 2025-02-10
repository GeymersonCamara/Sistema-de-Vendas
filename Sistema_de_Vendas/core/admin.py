from django.contrib import admin
from core.models import Evento, Cliente

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',)

admin.site.register(Evento, EventoAdmin)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')  # Mostra essas colunas no admin
    search_fields = ('nome', 'email')