from django.contrib import admin
from .models import Aluno, Treino, Instrutor

admin.site.site_header = "LOGIN FRANGO'S ACADEMY"
admin.site.site_title = 'ADMIN'
admin.site.index_title = 'ADMIN'

admin.site.register(Aluno)
admin.site.register(Treino)
admin.site.register(Instrutor)
