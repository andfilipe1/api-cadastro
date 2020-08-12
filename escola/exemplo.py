import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import validacpfcnpj

"""
Exemplo 1: Enviando CPF ao instanciar a classe
"""
cpf = validacpfcnpj.ValidaCpfCnpj('11111111111')

if cpf.valida():
    print('CPF %s é válido e foi formatado.' % cpf.formatado)
    print('CPF %s é válido e contém apenas números.' % cpf.cpf)
else:
    print('CPF inválido.')

"""
Exemplo 4: CPF Inválido
"""
cpf.cpf = '11111111111'

try:
    formatado = cpf.formatado
except ValueError:
    print("CPF inválido.")

