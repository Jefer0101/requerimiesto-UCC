from django.db import models

# Create your models here.

class Notificacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    extra_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)