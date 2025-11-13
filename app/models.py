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

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null= True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)

    def total (self):
        return self.quantidade*self.produto.preco