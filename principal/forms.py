'''
Created on 16 dic. 2020

@author: Manu
'''
#encoding:utf-8
from django import forms
from principal.models import Jugador, Ejercicio
    
class BusquedaEjercicios(forms.Form):
    lista1=[(j.tipo,j.tipo) for j in Ejercicio.objects.all()]
    lista2=[(j.objetivoTecnico,j.objetivoTecnico) for j in Ejercicio.objects.all()]
    lista3=[(j.objetivoTactico,j.objetivoTactico) for j in Ejercicio.objects.all()]
    tipo = forms.ChoiceField(label="Tipo", choices=lista1)
    objTecnico = forms.ChoiceField(label="Objetivo tecnico", choices=lista2)
    objTactico = forms.ChoiceField(label="Objetivo tactico", choices=lista3)
    
class BusquedaPartidosPorJugador(forms.Form):
    lista=[(j.id,j.nombre) for j in Jugador.objects.all()]
    jugador = forms.ChoiceField(label="Selecciona el jugador", choices=lista)