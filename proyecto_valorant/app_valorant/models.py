from distutils.command.upload import upload
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_campos(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')
        PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')

        errors = {}

        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email_exits'] = "Email ya registrado!!!"
        else:
            if len(postData['nombre'].strip()) < 2 or len(postData['nombre'].strip()) > 30:
                errors['first_name_len'] = "Nombre debe tener entre 2 y 30 caracteres"

            if len(postData['usuario'].strip()) < 2 or len(postData['usuario'].strip()) > 30:
                errors['last_name_len'] = "Apellido debe tener entre 2 y 30 caracteres"
            
            if not JUST_LETTERS.match(postData['nombre']):
                errors['just_letters'] = "Solo se permite el ingreso de letras en el nombre "
                
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Formato correo no válido"
            
            if not PASSWORD_REGEX.match(postData['contrasena']):
                errors['password_format'] = "Formato contraseña no válido"

       
        if postData['contrasena'] != postData['password_confirm']:
            errors['password_confirm'] = "Contraseñas no coinciden"

        return errors
        

class User(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=250)
    pais = models.CharField(max_length=30)
    edad = models.CharField(max_length=100)
    objects = UserManager()

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["email"]

    def __repr__(self) -> str:
        return self.nombre + "/" + self.usuario

class Contacto(models.Model):
    asunto=models.CharField(max_length=30)
    correo=models.EmailField(max_length=100)
    mensaje=models.TextField(max_length=500)


class mapas(models.Model):
    idusuario=models.CharField(max_length=30)
    mapa =models.CharField(max_length=30)
    aliminaciones = models.CharField(max_length=2)
    muertes = models.CharField(max_length=2)
    agente = models.CharField(max_length=30)
    rango = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="mapas")

class Creadores(models.Model):
    nombre=models.CharField(max_length=30)
    rango=models.CharField(max_length=30)
    estilo_juego=models.CharField(max_length=30)
    agente_main=models.CharField(max_length=30)