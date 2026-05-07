"""
PEP 8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python -- import this.

A ideia da PEP8 é que possamos escrever códigos Python
de forma Pythônica(forma bonita e visualmente agradável).

[1] -- Utilizar CamelCase para nomes de Classes;
class Calculadora:
    pass
class CalculadoraCientifica:
    pass
[2] -- Utilizar snake_case para funções ou variáveis.
def soma():
    pass
def soma_dois():
    pass
numero = 4
numero_impar = 5
[3] -- Utilizar 4 espaços para identação!
if 'a' in 'banana':
    print ('tem')
[4] -- 2 linhas em branco para definir uma classe
    Métodos dentro de uma classe devem ser separados
    com uma única linha em branco;
[5] -- Imports devem ser sempre feitos em linhas separadas;
import sys
import os
# Não ha problemas se pegar partes de um pacote. Ex:
from types import StringType, ListType
#Caso tenha muitos imports de um mesmo pacote, recomenda-se:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
Imports devem ser colocados no topo do arquivo, logo depois
de qualquer comentário ou docstrings e antes de constantes
ou variáveis globais
[6] -- Espaços em expressões e instruções
Não faça:
funcao( algo[ 1 ], { outro: 2 } )
Faça:
funcao(algo[1],{outro:2})
[7] -- Termine sempre uma instrução com uma nova linha em branco;

"""