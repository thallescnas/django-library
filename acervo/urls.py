from django.urls import path
from .views import list_livros, cadastrar_livro

urlpatterns=[
    path('', list_livros, name="livros"),
    path('cadastrar', cadastrar_livro, name="livro_cadastro")
]