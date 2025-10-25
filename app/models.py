from django.db import models

# Create your models here.
class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    email = models.EmailField(unique=True)   

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.CharField(max_length=600)