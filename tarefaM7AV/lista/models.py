from django.db import models
from datetime import datetime as dt

# Create your models here.


class ProjetoDjango(models.Model):


        filme_1 = models.CharField("Filme favorito #1", max_length=100)
        filme_2 = models.CharField("Filme favorito #2", max_length=100)
        filme_3 = models.CharField("Filme favorito #3", max_length=100)
        filme_4 = models.CharField("Filme favorito #4", max_length=100)
        filme_5 = models.CharField("Filme favorito #5", max_length=100)
        criado_em = models.DateTimeField(auto_now_add=True)
        data = models.DateTimeField("Publicado em", default=dt.now())

        def __str__(self):
            return f"Lista de {self.nome_usuario}"








