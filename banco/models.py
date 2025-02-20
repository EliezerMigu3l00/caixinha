from django.db import models
from datetime import date


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    data_criacao_cadastro = models.DateTimeField(auto_now_add=True)
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2)
       
    def idade(self):
        data_atual = date.today()
        return data_atual.year - self.data_nascimento.year - (
            (data_atual.month, data_atual.day)
        )


class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    data_solicitacao = models.DateTimeField(auto_now_add=True)


class CartaoCredito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cartoes_credito')
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
