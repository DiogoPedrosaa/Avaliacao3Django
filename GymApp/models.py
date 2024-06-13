from django.db import models


class Instrutor(models.Model):
    nome = models.CharField(max_length = 50, null = False)
    sobre = models.CharField(null = False, max_length = 200)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length = 50, null = False)
    cpf = models.CharField(max_length=14, null = False)
    objetivo = models.CharField(max_length = 200)
    sexo = models.CharField(max_length = 20)
    cep = models.CharField(max_length = 30, null = False)

    def __str__(self):
        return self.nome



class Treino(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    horario = models.DateTimeField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, default=1)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.tipo} - Aluno: {self.aluno.nome} - Instrutor: {self.instrutor.nome}"

    class Meta:
        verbose_name_plural = "Treinos"



    


    
