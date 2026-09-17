from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

# Create your views here.


def list_livros(request):
    livros_disponiveis = Livro.objects.filter(disponivel=True).order_by("-ano")

    return render(request,'acervo/list_livros.html', {"livros": livros_disponiveis})

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("livros")
    else:
        form = LivroForm()
    return render(request, "acervo/forms.html", {"form": form})
