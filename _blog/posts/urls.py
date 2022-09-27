from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sul/', views.sul, name='sul'),
    path('sudeste/', views.sudeste, name='sudoeste'),
    path('centro_oeste/', views.centro_oeste, name='centro_oeste'),
    path('norte/', views.norte, name='norte'),
    path('nordeste/', views.nordeste, name='nordeste'),
    path('post/<int:post_id>/', views.exibir_post, name='exibir_post'),
    path('autor/<int:autor_id>/', views.exibir_autor, name='exibir_autor'),
]
