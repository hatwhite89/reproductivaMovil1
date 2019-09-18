# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views import View

from reproductivaApp.models import MenuPrincipal,MenuRedesSociales,Post,ComentariosPost,Estado,ZonasCentroAyuda,CentroAyuda,Archivos,ImagenesGaleriaAlbum,AlbumGaleria,TelefonoCentroAyuda,PostContenido,Videos,PostContenidoSubCategoria,ContenidoSubCategoria,CategoriaPost
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from reproductivaApp.forms import FormularioRegistro,correo
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
    return HttpResponse("done")


# Create your views here.
#

def chat(request):
    usuario=request.user.username
    return render(request,"chat.html",{'usuario':usuario})

# Create your views here.

def main(request):

    return render(request,'index.html',)

#DEBE LISTAR TODAS LAS ZONAS PARA LOS CENTROS DE AYUDA
def zonas_list(request):
    zona_list = ZonasCentroAyuda.objects.all()
    return render(request,'zona_list.html',{'zonaList':zona_list})

#LISTA EL DETALLE DE LAS ZONAS, O SEA LOS CENTROS DE AYUDA
def zonas_detalle(request):
    id_zona= request.GET['id_zona']
    detalle_zona= CentroAyuda.objects.filter(zona=id_zona)

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
    usuario = request.POST['username']
    passwd = request.POST['password']


    user = authenticate(username=usuario, password=passwd)
    if user is None:
        return render(request, 'page-login.html', {"bandera":"ERROR"})
    else:

        return render(request,'page-login.html',{})

#VISTA PARA MOSTRAR TODAS LAS ENTRADAS DEL BLOG

def entradas_blog(request):
    return render(request,'home-blog.html')

class ListarEntradasBlog(ListView):

    model = Post
    template_name = 'home-blog.html'
    context_object_name = 'listPost'
    paginate_by = 2


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
            return render(request,'index.html',{'bandera':"verdadero"})
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


#el contenido nuevo
#VER UNA ENTRADA DEL BLOG
def verEntradaContenido(request):
    id_post=request.GET['id_post']
    entrada_blog =PostContenido.objects.filter(pk=id_post)
    return render(request,'contenido.html',{'post':entrada_blog})

def list_view_contenido(request):
    id_contenido= request.GET['id_contenido']
    lista_contenido_detalle=PostContenido.objects.filter(id_categoria=id_contenido)
    titulo = PostContenido.objects.filter(id_categoria=id_contenido)


    return render(request,'list_contenido.html',{'caList':lista_contenido_detalle,'titulo':titulo})

def conteido_detalle(request):

    id_archivo= request.GET['id_contenido']
    archivo_list= PostContenido.objects.filter(pk=id_archivo)

    return render(request,'contenido2.html',{'post':archivo_list})

def videos(request):
    list_video= Videos.objects.all()
    return render(request,'videos.html',{'videos':list_video})


#CONTENIDO CON SUBCATEGORIA
def list_view_contenido_subcategoria(request):
    id_contenido= request.GET['id_contenido']
    lista_contenido_detalle=ContenidoSubCategoria.objects.filter(categoriaPrincipal=id_contenido)



    return render(request,'list_contenido_sub.html',{'caList':lista_contenido_detalle})

def contenido_detalle_sub(request):
#ESTA ES OTRA LISTA

    id_archivo= request.GET['id_contenido']
    archivo_list= PostContenidoSubCategoria.objects.filter(id_categoria=id_archivo)
    return render(request,'list_contenido_sub2.html',{'post':archivo_list})

def post_contenido_detalle_sub(request):
#ESTOS SON LOS POST

    id_archivo= request.GET['id_contenido']
    archivo_list= PostContenidoSubCategoria.objects.filter(pk=id_archivo)
    return render(request,'contenido2.html',{'post':archivo_list})

def lista_categorias_blog(request):
    id_contenido = request.GET['id_contenido']
    lista_categoria= Post.objects.filter(id_categoria=id_contenido)
    return render(request,'lista_categoria_blog.html',{'lista_ca':lista_categoria})

def blog_detalle_tema(request):
#ESTOS SON LOS POST

    id_archivo= request.GET['id_contenido']
    archivo_list= Post.objects.filter(pk=id_archivo)
    return render(request,'contenido_detalle_blog.html',{'post':archivo_list})


class contacto(View):
    def get(self,request):
        form=correo()
        return render(request,'email.html',{'forma':form})

    def post(self,request):
        form=correo(request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            email=request.POST['correo']
            titulo=request.POST['asunto']
            contenid = request.POST['contenido']
            email = EmailMessage(titulo, contenid, to=['reproductivahn@gmail.com'])
            #email.body=form.contenido
            email.send()

            return HttpResponseRedirect('/salto_mensaje')

        return render(request,'email.html',{'forma':form})

def salto_mensaje(request):

    return render(request,'index.html',{'mensaje':'verdadero'})
