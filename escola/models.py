from django.db import models
import escola.validacpf



class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(), escola.validacpf.ValidaCpf()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
