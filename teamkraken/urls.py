"""teamkraken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from principal import views
from django.views import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jugadores/', views.jugadoresList, name='jugadores'),
    path('jugadores/jugador/<int:id_jugador>', views.jugadorDetails),
    path('partidos/', views.inicio),
    path('partidos/partido/<int:id_partido>/<int:id_jugador>', views.partidoDetails),
    path('entrenamientos/', views.entrenamientosList, name='entrenamientos'),
    path('entrenamientos/entrenamiento/<int:id_entrenamiento>', views.entrenamientoDetails),
    path('ejercicios/', views.buscar_ejerciciosporfiltro, name='ejercicios'),
    path('ejercicios/ejercicio/<int:id_ejercicio>', views.ejercicioDetails),
    path('media/<path>', static.serve, {'document_root':settings.MEDIA_ROOT,}),
    path('', views.inicio),
]
