from django import forms
from .models import Treino, Aluno, Instrutor
from django.contrib.auth.forms import AuthenticationForm

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['tipo', 'horario', 'aluno', 'instrutor']
        widgets = {
            'horario': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aluno'].queryset = Aluno.objects.all()
        self.fields['instrutor'].queryset = Instrutor.objects.all()

