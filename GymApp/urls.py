from django.urls import path
from . import views
from .views import ChecarTreinoListView, index, marcar_treino, Login, AlunoDetail
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='home'),
    path('marcar/', views.marcar_treino, name='marcar-treino'),
    path('checar/', ChecarTreinoListView.as_view(), name='checar-treino'),
    path('login/', Login.as_view(), name='login'),
    path('aluno/<int:pk>/', AlunoDetail.as_view(), name='aluno-detalhe'),
]