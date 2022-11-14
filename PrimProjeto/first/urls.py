from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registroUsuario, name='registro'),
    path('login', views.loginUsuario, name='login'),
    path('logout', views.logoutUsuario, name='logout'),
    path('perfilUsuario',views.perfilUsuario, name='perfilUsuario'),
    path('updateUsuario', views.updateUsuario, name='updateUsuario'),
    path('menu', views.menu, name='menu'),
    path('registroAvaliacao', views.registroAvaliacao, name='registroAvaliacao'),
    path('notificacoes', views.notificacoes, name='notificacoes'),
    path('notificacoesUsuario', views.notificacoesUsuario, name='notificacoesUsuario'),
    path('deletar', views.deletarPerfilUsuario, name="deletar"),
    path('encontro',views.encontrar,name='encontro'),
]
