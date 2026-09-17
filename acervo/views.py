from django.shortcuts import render
from .models import Livro

# Create your views here.


def list_livros(request):
    livros_disponiveis = Livro.objects.filter(disponivel=True).order_by("-ano")

    return render(request,'acervo/list_livros.html', {"livros": livros_disponiveis})
