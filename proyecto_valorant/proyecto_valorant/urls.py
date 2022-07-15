"""proyecto_valorant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_valorant import views


urlpatterns = [
    path('',views.index_web),
    path('admin/', admin.site.urls),
    path('registro_web/', views.registro_web),
    path('registro/', views.registro),
    path('login/',views.login),
    path('login_web/',views.login_web),
    path('contacto/',views.contacto),
    path('contacto_web/',views.contacto_web),
    path('jugadas/',views.jugadas),
    path('jugadas_web/',views.jugadas_web),
    path('listar_jugadas/',views.listar_jugadas),
    path('listar_jugadas_web/',views.listar_jugadas_web),
    path('creador_web/',views.registrar_creador_web),
    path('creadores/',views.creadores),
    path('listar_creador_web/',views.listar_creador_web),
    path('listar_creador/',views.listar_creador),
    path('base/',views.base),
    path('index_web/',views.index_web),
    path('agentes_web/',views.agentes_web),
    path('armas_web/',views.armas_web),
    path('entrar_jugadas_web/',views.entrar_jugadas),
    path('entrar_creadores_web/',views.entrar_creadores),
    path('nosotros_web/',views.nosotros_web),
    path('mapas_web/',views.mapas_web)
    

]
