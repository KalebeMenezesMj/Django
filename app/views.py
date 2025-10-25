from django.shortcuts import redirect,render
from app.models import Desenvolvedor, Contato

from app.forms import FormDesenvolvedor, FormContato, FormUsuario


def dev(request):
    devs = Desenvolvedor.objects.all().values()
    return render(request, 'desenvolvedores.html', {'desenvolvedores':devs})


def index(request):
    #return HttpResponse("Hello World!") # Exibe na tela
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


#DESENVOLVEDORES
def excluirDev(request, id_dev):
    dev = Desenvolvedor.objects.get(id=id_dev)
    dev.delete()
    return redirect('dev')


def salvarDev(request):
    formulario = FormDesenvolvedor(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('dev')

    return render(request, 'salvardev.html',{'form':formulario})


def editarDev(request, id_dev):
    dev = Desenvolvedor.objects.get(id=id_dev)
    formulario = FormDesenvolvedor(request.POST or None, instance=dev)
    if request.POST:
        if formulario.is_valid():
            formulario.save
            return redirect('dev')
    return render(request, 'editardev.html',{'form':formulario})


#MENSAGENS DE CONTATO
def readContato(request):
     contato = Contato.objects.all().values()
     return render(request, 'listcontato.html', {'contato':contato})

def salvarContato(request):
    formulario = FormContato(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('readContato')

    return render(request, 'contato.html',{'form':formulario})

def excluirContato(request, id_dev):
    msg = Contato.objects.get(id=id_dev)
    msg.delete()
    return redirect('readContato')


#USUARIOS
def salvarUsuario(request):
    if request.POST:
        formulario = FormUsuario(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
            formulario = FormUsuario()
    return render(request, 'salvar-usuario.html', {'form': formulario})
        