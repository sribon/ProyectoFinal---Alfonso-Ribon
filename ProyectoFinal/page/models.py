from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class articulo(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200,default="")
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(default='default.png',blank=True)
    autor = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.id},{self.titulo}"
