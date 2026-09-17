from django.urls import path
from .views import list_livros

urlpatters=[
    path('', list_livros, name="list_livros")
]