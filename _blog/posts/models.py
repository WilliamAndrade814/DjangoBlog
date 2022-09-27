from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Region(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(default='')
    regiao = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    imagem = models.TextField(default='')
    postado_em = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    conteudo = models.TextField(default='')
    area = models.TextField(default='')
    populacao = models.TextField(default='')
    capital = models.TextField(default='')


    def __str__(self):
        return self.titulo
