
# Create your models here.
# -*- coding: utf-8 -*-





from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# ESTADO EN GENERAL PARA LOS MODELOS
class Estado(models.Model):
    estado = models.CharField(max_length=20)
    fecha_creacion = models.DateField()
    def __str__(self):
        return self.estado





#SECCION DEL BLOG

class CategoriaPost(models.Model):
    categoria= models.CharField(max_length=200)
    descripcion= models.TextField()
    fecha_creacion=models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,)

    def __str__(self):
        return self.categoria






#SUBIR IMAGENES PARA GALERIAS

class CategoriaImagen(models.Model):
     categoria_imagen=models.CharField(max_length=200)

     def __str__(self):
         return self.categoria_imagen

class ImagenesGaleria(models.Model):
    titulo_imagen= models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='imagenes/')
    categoria_imagen=models.ForeignKey(CategoriaImagen, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo_imagen

#MENU PRINCIPAL PARA LAS PAGINAS
class MenuPrincipal(models.Model):
        nombre= models.TextField(max_length=200)
        tag_nombre= models.TextField(max_length=200)
        tag_url=models.TextField(max_length=200)
        icon_css = models.TextField(max_length=200)
        estado= models.BooleanField()

        def __str__(self):
            return self.nombre
#MENU DE REDES SOCIALES PARA LAS PAGINAS
class MenuRedesSociales(models.Model):
    nombre =models.TextField(max_length=200)
    tag_nombre= models.TextField(max_length=200)
    tag_url=models.TextField(max_length=200)
    icon_css=models.TextField(max_length=200)
    estado= models.BooleanField()

    def __str__(self):
        return self.nombre


#CENTROS DE ASISTENCIA
class ZonasCentroAyuda(models.Model):
      nombre_zona = models.TextField(max_length=150)
      def __str__(self):
          return  self.nombre_zona


class CentroAyuda(models.Model):
    nombre_centro_ayuda = models.CharField(max_length=200)
    imagen= models.ImageField(upload_to='imagenes/', null=True)
    direccion = models.TextField(max_length=250, null=True)
    sitio_web = models.TextField(max_length=100, null=True)
    email = models.EmailField(null=True)
    google_maps= models.TextField(null=True)
    zona= models.ForeignKey(ZonasCentroAyuda,  on_delete=models.CASCADE,)

    def __str__(self):
        return self.nombre_centro_ayuda


class TelefonoCentroAyuda(models.Model):
      telefono= models.TextField(max_length=20)
      centro_ayuda= models.ForeignKey(CentroAyuda, on_delete=models.CASCADE,)

      def __str__(self):
          return self.telefono


#MODELOS PARA LA SECCION DE RECURSOS

class Archivos(models.Model):

      nombre= models.TextField(max_length=150, null=True)
      descrip=models.TextField(null=True)
      fecha_publicacion=models.DateField()
      autor=models.TextField(max_length=150, null=True)
      usuario_creo=models.ForeignKey(User, on_delete=models.CASCADE,)
      archivo=models.FileField(upload_to='archivos/', null=True)

      def __str__(self):
          return self.nombre

#IMAGENES PARA GALERIA
class AlbumGaleria(models.Model):
    titulo_album=models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    descripcion=models.TextField()
    def __str__(self):
        return self.titulo_album

class ImagenesGaleriaAlbum(models.Model):
    titulo_imagen= models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='imagenes/')
    album=models.ForeignKey(AlbumGaleria, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo_imagen

#CONTENIDO DEL MENU

class CategoriaPostContenido(models.Model):
    categoria= models.CharField(max_length=200)
    descripcion= models.TextField()
    fecha_creacion=models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,)

    def __str__(self):
        return self.categoria

class PostContenido (models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    resumen= RichTextField(null=True)
    fecha_creacion =models.DateField()
    estado=models.ForeignKey(Estado ,on_delete=models.CASCADE,)
    imagen_portada=models.ImageField(upload_to='imagenes/', null=True)
    usuario_creo= models.ForeignKey(User,on_delete=models.CASCADE,)
    id_categoria=models.ForeignKey(CategoriaPostContenido, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo

class ContenidoSubCategoria (models.Model):
    categoria = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    categoriaPrincipal = models.ForeignKey(CategoriaPostContenido, on_delete=models.CASCADE, )

    def __str__(self):
        return self.categoria


class PostContenidoSubCategoria (models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    resumen= RichTextField(null=True)
    fecha_creacion =models.DateField()
    estado=models.ForeignKey(Estado ,on_delete=models.CASCADE,)
    imagen_portada=models.ImageField(upload_to='imagenes/', null=True)
    usuario_creo= models.ForeignKey(User,on_delete=models.CASCADE,)
    id_categoria=models.ForeignKey(ContenidoSubCategoria, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo

class Videos(models.Model):
    titulo = models.CharField(max_length=200)
    url=models.TextField()
    fecha_publicacion=models.DateField()

#NOTICIAS
class Noticias (models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    resumen= RichTextField(null=True)
    fecha_creacion =models.DateField()

    imagen_portada=models.ImageField(upload_to='imagenes/', null=True)



    def __str__(self):
        return self.titulo

#BLOGUEROS
class Bloguero (models.Model):
    nombre = models.CharField(max_length=200,null=True)
    descripcion =models.TextField(null=True)
    foto=models.ImageField(upload_to='imagenes/', null=True)
    def __str__(self):
        return self.nombre

#POST DEL BLOG
class Post (models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    resumen= RichTextField(null=True)
    fecha_creacion =models.DateField()
    estado=models.ForeignKey(Estado ,on_delete=models.CASCADE,)
    imagen_portada=models.ImageField(upload_to='imagenes/', null=True)
    bloguero= models.ForeignKey(Bloguero,on_delete=models.CASCADE,)
    id_categoria=models.ForeignKey(CategoriaPost, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo

    # COMENTARIOS DE POST
class ComentariosPost(models.Model):
    cuerpo = RichTextField()
    fecha_publicacion = models.DateField()
    usuario = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, )
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, )

#COMENTARIOS DE CONTENIDO
class ComentariosPostContenido(models.Model):
    cuerpo = RichTextField()
    fecha_publicacion = models.DateField()
    usuario = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, )
    id_post = models.ForeignKey(PostContenido, on_delete=models.CASCADE, )

class DudasFrecuentes(models.Model):
        pregunta= RichTextField()
        respuesta=RichTextField()
        fecha_publicacion=models.DateField()
        usuario_registro=models.ForeignKey(User,on_delete=models.CASCADE,)

        def __str__(self):
            return self.pregunta

