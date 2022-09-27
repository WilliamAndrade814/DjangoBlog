from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',
                  {'posts': posts[::-1]})


def sul(request):
    posts = Post.objects.filter(regiao='1')
    return render(request, 'index.html',
                  {'posts': posts[::-1]})


def sudeste(request):
    posts = Post.objects.filter(regiao='2')
    return render(request, 'index.html',
                  {'posts': posts[::-1]})


def centro_oeste(request):
    posts = Post.objects.filter(regiao='3')
    return render(request, 'index.html',
                  {'posts': posts[::-1]})


def nordeste(request):
    posts = Post.objects.filter(regiao='4')
    return render(request, 'index.html',
                  {'posts': posts[::-1]})


def norte(request):
    posts = Post.objects.filter(regiao='5')
    return render(request, 'index.html',
                  {'posts': posts[::-1]})


def exibir_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'exibir_post.html',
                  {'post': post})


def exibir_autor(request, autor_id):
    posts = Post.objects.filter(autor=autor_id)
    return render(request, 'index.html',
                  {'posts': posts[::-1]})
