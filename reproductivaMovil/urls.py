
"""reproductiva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import logout

from reproductivaMovil import settings
from reproductivaApp import views
from django.conf.urls.static import static
from django.contrib.auth.views import auth_login, logout_then_login, auth_logout, LoginView, LogoutView

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^chat/$', views.chat, name="chat"),
    url(r'^listarAlbum/$', views.listarAlbumes, name="listarAlbum"),
    url(r'^album/$', views.mostrarAlbum, name="Album"),
    url(r'^agradecimiento/$', views.agradecimientos, name="agradecimiento"),
    url(r'^ajax/chat/$', views.broadcast),
    url(r'^admin/', admin.site.urls),
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^entrada_blog_list/$', views.listar_entradas_blog, name="entrada_blog_list"),
    url(r'^archivos_list/$', views.archivos, name="archivos_list"),
    url(r'^archivos_detalle/$', views.archivos_detalle, name="archivos_detalle"),
    url(r'^zonas_list/$', views.zonas_list, name="zonas_list"),
    url(r'^zonas_detalle/$', views.zonas_detalle, name="zonas_detalle"),
    url(r'^centro_ayuda/$', views.centro_ayuda, name="centro_ayuda"),
    url(r'^entrada_blog/$', views.verEntradaBlog, name="entrada_blog"),
    url(r'^entrada_contenido/$', views.verEntradaContenido, name="entrada_contenido"),
    url(r'^comentario_blog/$', views.agregarComentarioBlog, name="comentario_blog"),
    url(r'^videos/$', views.videos, name="videos"),
    url(r'^listar_contenido/$', views.list_view_contenido, name="listar_contenido"),
    url(r'^listar_contenido_sub2/$', views.contenido_detalle_sub, name="listar_contenido_sub2"),
    url(r'^listar_contenido2/$', views.list_view_contenido_subcategoria, name="listar_contenido2"),
    url(r'^contenido_detalle/$', views.conteido_detalle, name="contenido_detalle"),
    url(r'^contenido_detalle_sub/$', views.contenido_detalle_sub, name="contenido_detalle_sub"),
    url(r'^post_contenido_detalle_sub/$', views.post_contenido_detalle_sub, name="post_contenido_detalle_sub"),
    url(r'^lista_categoria_blog/$', views.lista_categorias_blog, name="lista_categoria_blog"),
    url(r'^blog_detalle_tema/$', views.blog_detalle_tema, name="blog_detalle_tema"),
    url(r'^blog_list/(?P<id_post>\w{0,50})/$', views.entradas_blog, name="blog_list"),
    url(r'^login/$', LoginView.as_view(template_name='page-login.html'), name='login'),


    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    url(r'^registrar/$', views.registrar, name="registrar"),
    url(r'^listaPost/$', views.listar_entradas_blog, name="listaPost"),

]
# SI EL DEBUG ES TRUE ENTONCES QUE TOME LA CARPETA STATIC_URL, DE LO CONTRARIO QUE UTILIZE LA CARPETA MEDIA_URL
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
