# Generated by Django 5.0 on 2024-06-13 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0002_alter_aluno_cpf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treino',
            options={'verbose_name_plural': 'Treinos'},
        ),
        migrations.AddField(
            model_name='treino',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GymApp.aluno'),
        ),
    ]
