#!/usr/bin/env python

from decouple import config


var = config('VAR_CHAR')

print(var)

var2 = config('SAMUKA')
print(var2)

boleano_1 = config('VAR_BOOL')

if boleano_1:
    print("valor Verdadeiro")
else:
    print("valor Falso")
print(type(boleano_1))

boleano = config('VAR_BOOL', cast=bool)

if boleano:
    print("valor Verdadeiro")
else:
    print("valor Falso")
print(type(boleano))

numero = config('VAR_NUM', default=123)
print(numero)

numero_2 = config('VAR_INT', cast=int)
print(numero_2)
print(type(numero_2))
