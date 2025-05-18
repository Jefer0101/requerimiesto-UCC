from django.forms import forms
from django.forms import ModelForm
from .models import Notificacion

class NotificacionForm(ModelForm):
    class Meta:
        model = Notificacion
        fields = ['title', 'description', 'extra_details']
