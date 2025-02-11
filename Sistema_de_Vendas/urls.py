"""
URL configuration for Sistema_de_Vendas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.pag_inicio, name='agenda'),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('principal/', views.lista_eventos, name='principal'),
    path('logout/', views.logout_user),
    path('clientes/', views.cad_clientes, name='clientes'),
    path('produtos/', views.cad_produtos, name='produtos'),
    path('mercado/', views.pag_mercado, name='mercado'),
]