# Generated by Django 5.1.1 on 2024-09-24 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('telefone', models.CharField(max_length=20)),
                ('data_criacao_cadastro', models.DateTimeField(auto_now_add=True)),
                ('renda_mensal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite_credito', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_emprestimo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cliente')),
            ],
        ),
    ]
