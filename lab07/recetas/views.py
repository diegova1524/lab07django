from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Usuario, RegistroEvento
from .forms import EventoForm, RegistroForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def registrar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.evento = evento
            registro.save()
            return redirect('detalle_evento', evento_id=evento_id)
    else:
        form = RegistroForm()
    return render(request, 'registrar_evento.html', {'form': form, 'evento': evento})

# Implementa otras vistas para actualizar y eliminar eventos y registros de eventos
