import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import escola.validacpf

"""
Exemplo 1: Enviando CPF ao instanciar a classe
"""

#cpf =  validacpf.ValidaCpf(('12235521797'))
cpf =  escola.validacpf.ValidaCpf(('111111111111'))

if cpf.valida():
    print('CPF %s é válido e foi formatado.' % cpf.formatado)
    print('CPF %s é válido e contém apenas números.' % cpf.cpf)
else:
    print('CPF inválido.')





