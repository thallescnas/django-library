from django.db import models

# Create your models here.



class Livro(models.Model):
    CATE_CHOICES = [
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
    TIPOS_CHOICES = (
        ("digital", "Livro digital"),
        ("fisico", "Livro fisico")
    )
    titulo = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=200, blank=False, null=False)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    categoria = models.CharField(max_length=100, choices=CATE_CHOICES, default=000)
    tipo = models.CharField(max_length=35, choices=TIPOS_CHOICES, default="digital")

    def __str__(self):
        return self.titulo