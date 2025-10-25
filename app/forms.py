from django import forms
from app.models import Desenvolvedor
from app.models import Contato
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