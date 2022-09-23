from ckeditor_uploader.fields import RichTextUploadingField
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
    imagem = RichTextUploadingField()
    postado_em = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=40)
    conteudo = models.TextField(default='')

    def __str__(self):
        return self.titulo
