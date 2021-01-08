'''
Created on 16 dic. 2020

@author: Manu
'''
#encoding:utf-8
from django import forms
from principal.models import Jugador, Ejercicio, ObjetivoTecnico,\
    ObjetivoTactico
    
class BusquedaEjercicios(forms.Form):
    lista2=[(j.id,j.nombre) for j in ObjetivoTecnico.objects.all()]
    lista3=[(j.id,j.nombre) for j in ObjetivoTactico.objects.all()]
    objTecnico = forms.ChoiceField(label="Objetivo tecnico", choices=lista2)
    objTactico = forms.ChoiceField(label="Objetivo tactico", choices=lista3)
    
#class BusquedaPartidosPorJugador(forms.Form):
#    lista=[(j.id,j.nombre) for j in Jugador.objects.all()]
#    jugador = forms.ChoiceField(label="Selecciona el jugador", choices=lista)