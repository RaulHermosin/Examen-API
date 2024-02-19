from django.db import models

# Create your models here.

class usuario(models.Model):
    DNI = models.CharField(primary_key=True)
    numsocio = models.IntegerField(blank= False)
    contraseña = models.CharField(max_length=20, blank= False)