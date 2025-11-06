from django import forms
from app.models import Desenvolvedor
from app.models import Contato, Produto, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormDesenvolvedor(forms.ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = '__all__'

class FormContato(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = ("__all__")

class FormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username':'Usuario',
            'email':'E-mail',
        }

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields= ['nome', 'descricao', 'preco', 'imagem','categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'seu nome aqui'}),
            'imagem': forms.FileInput(attrs={'accept':'image/*'})
        }