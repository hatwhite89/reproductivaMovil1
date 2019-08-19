from django.contrib import admin

# Register your models here.

# -*- coding: utf-8 -*-

from django.db import models
#from models import CentroAyuda,Post,CategoriaPost,Estado,CategoriaImagen,ImagenesGaleria,MenuPrincipal,MenuRedesSociales,ComentariosPost,ZonasCentroAyuda,Archivos,AlbumGaleria,ImagenesGaleriaAlbum,TelefonoCentroAyuda
from django.contrib import admin

# Register your models here.
from reproductivaApp.models import CentroAyuda,Post,CategoriaPost,Estado,CategoriaImagen,ImagenesGaleria,MenuPrincipal,MenuRedesSociales,ComentariosPost,ZonasCentroAyuda,Archivos,AlbumGaleria,ImagenesGaleriaAlbum,TelefonoCentroAyuda


admin.site.register(CentroAyuda)
admin.site.register(Post)
admin.site.register(CategoriaPost)
admin.site.register(Estado)
admin.site.register(CategoriaImagen)
admin.site.register(ImagenesGaleria)
admin.site.register(MenuRedesSociales)
admin.site.register(MenuPrincipal)
admin.site.register(ComentariosPost)
admin.site.register(ZonasCentroAyuda)
admin.site.register(Archivos)
admin.site.register(AlbumGaleria)
admin.site.register(ImagenesGaleriaAlbum)
admin.site.register(TelefonoCentroAyuda)

