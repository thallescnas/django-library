from django.db import models

# Create your models here.


class Tipo(models.Model):
    status = (
        ("digital", "Livro digital"),
        ("fisico", "Livro fisico")
    )

    tipo = models.CharField(max_length=15, choices=status, blank=False, null=False)

    def __str__(self):
        return self.tipo

class Categoria(models.Model):
    status = [
        ("000", "Generalidades e Informação: Obras gerais, enciclopédias, jornais e biblioteconomia."),
        ("100", "Filosofia e Psicologia: Ética, lógica e investigações sobre a mente humana."),
        ("200", "Religião e Teologia: Mitologia, teologia e estudos sobre crenças e religiões."),
        ("300", "Ciências Sociais e Direito: Política, economia, sociologia, educação e leis."),
        ("400", "Linguística e Idiomas: Gramáticas, dicionários e estudos de línguas."),
        ("500", "Ciências Puras (Exatas e Naturais): Matemática, física, química, biologia e astronomia."),
        ("600", "Ciências Aplicadas (Tecnologia): Medicina, engenharia, agricultura e administração."),
        ("700", "Artes e Recreação: Pintura, música, arquitetura, esportes e lazer."),
        ("800", "Literatura: Poesia, romances, contos, crônicas e crítica literária."),
        ("900", " História e Geografia: Biografias, viagens e acontecimentos históricos")
    ]
    categorias = models.CharField(max_length=200, choices=status, null=False, blank=False)
class Livro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=200, blank=False, null=False)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, blank=False, null=False, default="digital", on_delete=models.CASCADE)