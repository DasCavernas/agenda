from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here

def eventos(request, nome_evento):
    local = Evento.objects.get(titulo=nome_evento)
    return HttpResponse(f'{local}')

#def index(request):
    #return redirect('/agenda/')


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

