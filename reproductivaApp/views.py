# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from reproductivaApp.models import MenuPrincipal,MenuRedesSociales,Post,ComentariosPost,Estado,ZonasCentroAyuda,CentroAyuda,Archivos,ImagenesGaleriaAlbum,AlbumGaleria,TelefonoCentroAyuda
from  django.http import  HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from reproductivaApp.forms import FormularioRegistro
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

#import the user library
from pusher import Pusher
#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
pusher = Pusher(app_id=u'838312', key=u'c230b932004655cce3ff', secret=u'ab9b3c8e1c7fb642c692',cluster='us2')

@csrf_exempt
def broadcast(request):

    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");


# Create your views here.
#
@login_required()
def chat(request):
    usuario=request.user.username
    return render(request,"chat.html",{'usuario':usuario});

# Create your views here.

def main(request):
    menu_principal= MenuPrincipal.objects.all()
    menu_redes=MenuRedesSociales.objects.all()

    return render(request,'index.html',{'menu_list': menu_principal,'redes_list': menu_redes})

#DEBE LISTAR TODAS LAS ZONAS PARA LOS CENTROS DE AYUDA
def zonas_list(request):
    zona_list = ZonasCentroAyuda.objects.all()
    return render(request,'zona_list.html',{'zonaList':zona_list})

#LISTA EL DETALLE DE LAS ZONAS, O SEA LOS CENTROS DE AYUDA
def zonas_detalle(request):
    id_zona= request.GET['id_zona']
    detalle_zona= CentroAyuda.objects.filter(pk=id_zona)

    return  render(request,'zona_detalle.html',{'detalleZona':detalle_zona})

#DEBE LISTAR TODOS CENTROS DE AYUDA DE UNA ZONA
def centro_ayuda(request):
    id_ca= request.GET['id_ca']
    centro_ayuda_detalle= CentroAyuda.objects.filter(pk=id_ca)
    telefonos=TelefonoCentroAyuda.objects.filter(centro_ayuda=id_ca)

    return render(request,'centros_ayuda.html',{'caList':centro_ayuda_detalle,'telList':telefonos})

def post_list(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request,'page-login.html',{})

#VISTA PARA MOSTRAR TODAS LAS ENTRADAS DEL BLOG

def entradas_blog(request):
    return render(request,'home-blog.html')

class ListarEntradasBlog(ListView):

    model = Post
    template_name = 'home-blog.html'
    context_object_name = 'listPost'
    paginate_by = 5


def listar_entradas_blog(request):
    list_entradas=Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(list_entradas, 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'home-blog.html', { 'listPost': users})

#REGISTRAR CUENTA
def registrar(request):
    form = FormularioRegistro(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    form = FormularioRegistro()
    return render(request,'page-signup.html',{'form':form})

#VER UNA ENTRADA DEL BLOG
def verEntradaBlog(request):
    id_post=request.GET['id_post']
    entrada_blog =Post.objects.filter(pk=id_post)
    comentarios_post= ComentariosPost.objects.filter(id_post=id_post)
    contador_comentarios= ComentariosPost.objects.filter(id_post=id_post).count()


    return render(request,'blog-post.html',{'post':entrada_blog,'id_post':id_post,'comentariosList':comentarios_post,'contador':contador_comentarios})
@login_required()
def agregarComentarioBlog(request):

    id_post = request.GET['id_post']
    id_objeto_post=Post.objects.get(pk=id_post)
    entrada_blog = Post.objects.filter(pk=id_post)
    newComentario = ComentariosPost(estado=Estado.objects.get(id=1),
                                    cuerpo= request.GET['cuerpo'],
                                    fecha_publicacion=time.strftime("%Y-%m-%d"),
                                    usuario=request.user,
                                    id_post=id_objeto_post)

    newComentario.save()
    comentarios_post = ComentariosPost.objects.filter(id_post=id_post)
    return render(request,'blog-post.html',{'post':entrada_blog,'id_post':id_post,'comentariosList':comentarios_post})


#VISTA PARA LOS ARCHIVOS

def archivos(request):
    archivo_list =Archivos.objects.all()
    return render(request,'archivos.html',{'detalleArchivo':archivo_list})

def archivos_detalle(request):

    id_archivo= request.GET['id_archivo']
    archivo_list= Archivos.objects.filter(pk=id_archivo)
    return render(request,'archivos_detalle.html',{'detalleArchivo':archivo_list})

#VISTA PARA LISTAR LOS ALBUMES

def listarAlbumes(request):
    list_album=AlbumGaleria.objects.all()
    return render(request,'albumes_list.html',{'albumList':list_album})

def mostrarAlbum(request):
    id_album = request.GET['id_album']
    album_detalle= ImagenesGaleriaAlbum.objects.filter(album=id_album)

    return render(request,'album.html',{'listaImagenes':album_detalle})

def agradecimientos(request):


    return render(request,'agradecimiento.html')