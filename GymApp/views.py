from django.shortcuts import render
from .forms import TreinoForm
from django.views.generic import ListView, TemplateView, DetailView
from .models import Treino, Aluno
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class LoginRequiredMixinView(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

class ChecarTreinoListView(LoginRequiredMixinView, ListView):
    model = Treino
    template_name = 'gym/checartreinos.html'
    context_object_name = 'treinos'

class IndexView(LoginRequiredMixinView, TemplateView):
    template_name = 'gym/index.html'

@login_required(login_url='login')
def index(request):
    return render(request, 'gym/index.html')

@login_required(login_url='login')
def marcar_treino(request):
    success_message = ''
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Treino Marcado com Sucesso, Parabens Monstro!'
            form = TreinoForm()
    else:
        form = TreinoForm()
    return render(request, 'gym/marcartreinos.html', {'form': form, 'success_message': success_message})

class Login(AuthLoginView):
    template_name = 'gym/login.html'


class AlunoDetail(DetailView):
    model = Aluno
    template_name = 'gym/aluno_detalhe.html'
    context_object_name = 'aluno'
