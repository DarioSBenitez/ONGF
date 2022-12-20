from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Principal(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True     # Para añadir estos atributos como eredados y que la clase
                            #no se registre en la base de datos

# CLASES QUE EREDAN ATRIBUTOS!!

class Categoria(Principal):
    nombre = models.CharField('Nombre de la categoria', max_length=100, unique=True) 
    imagen = models.ImageField('Imagen', upload_to='categoria/')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

    
class Autor(Principal):
    nombre = models.CharField('Nombres',max_length=100)
    apellido = models.CharField('Apellido',max_length=100)
    email = models.EmailField('Email',max_length=150)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.Format(self.apellido, self.nombre)

class Noticia(Principal):
    titulo = models.CharField('Titulo de la noticia',max_length=200, unique= True)
    slug = models.CharField('Slug',max_length=200, unique=True)
    descripcion = models.TextField('Descripcion')
    Categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    # imagen = models.ImageField('imagen', upload_to = 'imagenes/', max_length) ver aa¡ca el error
    



    