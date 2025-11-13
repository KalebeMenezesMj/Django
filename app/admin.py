from django.contrib import admin
from app.models import Categoria, Produto, Compra
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display =("nome",)

class CompraAdmin(admin.ModelAdmin):
    list_display =("produto","quantidade","data","total")

class ProdutoAdmin(admin.ModelAdmin):
    list_display =("nome","descricao","preco","imagem", "estoque", "categoria")

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Compra, CompraAdmin)