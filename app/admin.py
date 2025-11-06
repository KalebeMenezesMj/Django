from django.contrib import admin
from app.models import Categoria
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display =("nome",)

admin.site.register(Categoria, CategoriaAdmin)