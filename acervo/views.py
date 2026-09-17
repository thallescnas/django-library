from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Livro
from .forms import LivroForm

# Create your views here.


def list_livros(request):
    busca = request.GET.get('buscalibros', '')
    livros = Livro.objects.all()

    if busca:
        livros = livros.filter(
            Q(titulo__icontains=busca)
            | Q(tipo__icontains=busca)
            | Q(categoria__icontains=busca)
        )
    return render(request, 'acervo/list_livros.html', {"livros": livros, "libro": redirect("livro")})

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("livros")
    else:
        form = LivroForm()
    return render(request, "acervo/forms.html", {"form": form, "libro": redirect("livro")})
