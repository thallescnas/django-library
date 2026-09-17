from django.urls import path
from .views import list_livros

urlpatterns=[
    path('', list_livros, name="list_livros")
]