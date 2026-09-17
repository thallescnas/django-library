from django.contrib import admin
from .models import Livro, Categoria, Tipo

# Register your models here.

admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Tipo)