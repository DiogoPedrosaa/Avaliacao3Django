# Generated by Django 5.0 on 2024-06-13 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0003_alter_treino_options_treino_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='treino',
            name='instrutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GymApp.instrutor'),
        ),
    ]
