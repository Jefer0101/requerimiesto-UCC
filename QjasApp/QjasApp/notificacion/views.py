from django.shortcuts import render, redirect
from .models import Notificacion
from .forms import NotificacionForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def notificacion(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'notificaciones.html', {
        'notificaciones': notificaciones
    })

def createNotificacion(request):
    form = NotificacionForm()

    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            newNotificacion = Notificacion.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                extra_details = form.cleaned_data['extra_details']
            )
            newNotificacion.save()
            return redirect('notificacion')

    return render(request, 'creation_notificacion.html', {
        'form': form
    })




def deleteNotificacion(request, pk):
    noti = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        noti.delete()
        messages.success(request, "Notificación eliminada correctamente.")
        return redirect('notificacion')
    return render(request, 'confirm_delete.html', {'notificacion': noti})

