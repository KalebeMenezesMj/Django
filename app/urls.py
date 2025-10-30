from django.urls import path
from . import views # Do diretório do projeto, pega o arquivo views

urlpatterns = [
    path('', views.index, name='index'), # Pega a função dentro do view, ja o name é o nome da url/rota
    path('sobre', views.sobre, name='sobre'),


    #crud dev
    path('desenvolvedores', views.dev, name='dev'),
    path('excluir-dev/<int:id_dev>', views.excluirDev, name='excluirDev'),
    path('salvar-dev/', views.salvarDev, name='salvarDev'),
    path('editar-dev/<int:id_dev>', views.editarDev, name='editarDev'),


    #crud contato
    path('contato', views.salvarContato, name='contato'),
    path('listcontato', views.readContato, name='readContato'),
    path('excluirContato/<int:id_dev>', views.excluirContato, name='excluirContato'),


    #crud usuario
    path('salvar-usuario', views.salvarUsuario, name='salvarUsuario'),
    path('login', views.loginUsuario, name='login')

]