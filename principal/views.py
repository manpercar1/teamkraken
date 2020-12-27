#encoding:utf-8
from django.shortcuts import render, get_object_or_404
from principal.models import Jugador, Partido, TestCooper, Entrenamiento, Ejercicio
from django.conf import settings
from principal.forms import BusquedaPartidosPorJugador, BusquedaEjercicios
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def jugadoresList(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})

def jugadorDetails(request, id_jugador):
    jugador = get_object_or_404(Jugador, pk=id_jugador)
    entrenamientos = Entrenamiento.objects.filter(jugadores=id_jugador)
    partidos = Partido.objects.filter(jugador=id_jugador)
    testCooper = TestCooper.objects.filter(jugador=id_jugador)
    #partidos
    #test de cooper
    return render(request, 'jugadorDetails.html', {'jugador': jugador, 'entrenamientos': entrenamientos, 'partidos': partidos,
                                                    'testCoopers': testCooper})

def partidoDetails(request, id_partido, id_jugador):
    partido = get_object_or_404(Partido, pk=id_partido)
    jugador = get_object_or_404(Jugador, pk=id_jugador)
    return render(request, 'partidoDetails.html', {'partido': partido, 'jugador': jugador})

def entrenamientosList(request):
    entrenamientos = Entrenamiento.objects.all()
    return render(request, 'entrenamientos.html', {'entrenamientos': entrenamientos})

def entrenamientoDetails(request, id_entrenamiento):
    entrenamiento = get_object_or_404(Entrenamiento, pk=id_entrenamiento)
    return render(request, 'entrenamientoDetails.html', {'entrenamiento': entrenamiento})

def ejerciciosList(request):
    ejercicios = Ejercicio.objects.all()
    return render(request, 'ejercicios.html', {'ejercicios': ejercicios})

def ejercicioDetails(request, id_ejercicio):
    ejercicio = get_object_or_404(Ejercicio, pk=id_ejercicio)
    return render(request, 'ejercicioDetails.html', {'ejercicio': ejercicio, 'MEDIA_URL':settings.MEDIA_URL})

def buscar_partidosporjugador(request):
    formulario = BusquedaPartidosPorJugador()
    partidos = None
    jugador = None
    
    if request.method=='POST':
        formulario = BusquedaPartidosPorJugador(request.POST)      
        if formulario.is_valid():
            jugador=Jugador.objects.get(id=formulario.cleaned_data['jugador'])
            partidos = jugador.partido_set.all()
            
    return render(request, 'partidos.html', {'formulario':formulario, 'partidos':partidos, 'jugador':jugador})

def buscar_ejerciciosporfiltro(request):
    formulario = BusquedaEjercicios()
    resultado = None
    
    if request.method=='POST':
        formulario = BusquedaEjercicios(request.POST)      
        if formulario.is_valid():
            resultado = Ejercicio.objects.filter(objetivoTecnico=formulario.cleaned_data['objTecnico'], 
                                                  objetivoTactico=formulario.cleaned_data['objTactico'])
    
    ejercicios = Ejercicio.objects.all()
    return render(request, 'ejercicios.html', {'formulario':formulario, 'resultado':resultado, 'ejercicios': ejercicios})


#PARA CREAR UN ENTRENAMIENTO, A�ADIR "CREAR ENTRENAMIENTO" A LA VISTA DE EJERCICIOS.
#CUANDO SE CREE UN ENTRENAMIENTO QUE NO SE A�ADA NI JUGADORES NI FALTAS (PONER NULLABLE EN MODELO SI ES NECESARIO QUE AUN NO LO SE)
#PARA A�ADIR LISTA DE ASISTENCIA A LOS ENTRENAMIENTOS, A�ADIR BOTON "EDITAR ENTRENAMIENTO" EN LA VISTA DE DETALLES DE UN ENTRENAMIENTO
#PARA A�ADIR LAS FALTAS A LOS ENTRENAMIENTOS, PONER UN BOTON "A�ADIR FALTA"

#POSIBLE IDEA PARA LOS PARTIDOS:
#EN LA VISTA PARTIDOS, PONER UN BOTON QUE SEA A�ADIR NUEVO PARTIDO Y QUE MUESTRE UNA LISTA DE TODOS LOS JUGADORES. AL LADO DE CADA JUGADOR
#HABR� UN BOTON PARA A�ADIR A LA LISTA DE CONVOCADOS QUE LO QUE HAR� SER� CREAR UN PARTIDO VAC�O PARA CADA JUGADOR. DESPU�S DEL PARTIDO, HABR�
#QUE IR JUGADOR POR JUGADOR CAMBIANDO SUS ESTAD�STICAS DEL PARTIDO 

    