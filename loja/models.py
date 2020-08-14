from django.db import models
from cpf_field.models import CPFField

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = CPFField('cpf')
    data_inclusao = models.DateField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    nome = models.CharField(max_length=30)
    codigo_produto = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    #nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B')

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):
    TIPO = (
        ('M', 'Pessoa-Fisica'),
        ('V', 'Pessoa-Juridica'),
        ('N', 'Nao-Declarado')
    )
    nome = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False,default='V')
    CNPJ = models.CharField(max_length=11)

    